from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import json

from datetime import datetime
from typing import List

from .serializers import CountrySerializer, CountriesSerializer
from .models import Country
from .countriesPaginator import CountriesPaginator


def getCountryById(countryId: int) -> Country | None:
    """
    Retrieves a Country with given ID (if exists).

    Parameters:
        countryId (int): ID of a wanted Country.

    Returns:
        Country | None: Country with given ID or None.
    """
    try:
        return Country.objects.get(id = countryId)
    except Country.DoesNotExist:
        return None

def filterCountries(request) -> List[Country]:
    """
    Retrieves all Country entities which fulfull given filter (if provided).

    Parameters:
        request (Request): HTTP Request.

    Returns:
        List[Country]: _description_
    """
    filter: str | None= request.GET.get("country-code")
    
    return (
        Country.objects.filter(countryCode=filter)
        if (filter is not None)
        else Country.objects.all()
    )


class CountriesIdentifiableView(APIView):
    """
    View for "/countries/<id>" endpoint.
    """
    
    def get(self, request, country_id):
        """
        Retrieves data of a Country with give `country_id``.
        
        Parameters:
            request (Request): HTTP request
            country_id (int): ID of a Country.
            
        Returns:
            Data of wanted Country.
        """
        country = getCountryById(country_id)
        if country is None:
            return Response(status=404)
        
        serializer = CountrySerializer(country)
        return Response(status=200, data=serializer.data)
    
    
    
    def put(self, request, country_id):
        """
        Updates data of a Country with given ``country_id``.

        Parameters:
            request (Request): HTTP Request.
            country_id (int): ID of a Country.
            
        Returns:
            Data of updated Country.
        """
        country = getCountryById(country_id)
        if country is None:
            return Response(status=404)
        
        newData = json.loads(request.body)
        serializer = CountrySerializer(country, data=newData, partial=True)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=200, data=serializer.data)
            
        return Response(status=404)


class CountriesBaseView(APIView):
    """
    View for "/countries" endpoint.
    """
        
    def get(self, request):
        """
        Retrieves a list of Country entities. 
        Filter of country code and pagination limit & offset can be applied.

        Parameters:
            request (Request): HTTP request

        Returns:
            List of Country entities with Pagination and Links.
        """
        paginator = CountriesPaginator()        
        
        countries = filterCountries(request)        
        data = paginator.getpaginatedData(request, countries)
        
        serializer = CountriesSerializer(data)
        return Response(serializer.data)
        
    
    def post(self, request):
        """
        Creates a new Country entity.

        Parameters:
            request (Request): HTTP request

        Returns:
            Data of newly created Country.
        """
        data = json.loads(request.body)
        
        data["createdAt"] = datetime.now()
        data["groupId"] = 1
        
        serializer = CountrySerializer(data=data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=201, data=serializer.data)

        return Response(status=500)
        
        
    
        
