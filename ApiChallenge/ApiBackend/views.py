from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
import json

from datetime import datetime

from . import serializers
from . import models
from .countriesPaginator import CountriesPaginator


def getCountryById(countryId: int) -> models.Country | None:
    try:
        return models.Country.objects.get(id = countryId)
    except models.Country.DoesNotExist:
        return None

def filterCountries(request):
    hasFilter: bool = request.GET.get("CountryCodeFiltr") is not None
    
    return (
        models.Country.objects.filter(countryCode=request.GET.get("CountryCodeFiltr"))
        if hasFilter
        else models.Country.objects.all()
    )


class CountriesIdentifiableView(APIView):
    def get(self, request, country_id):
        country = getCountryById(country_id)
        if country is None:
            return Response(status=404)
        
        serializer = serializers.CountrySerializer(country)
        return Response(serializer.data)
    
    
    def put(self, request, country_id):
        country = getCountryById(country_id)
        if country is None:
            return Response(status=404)
        
        newData = json.loads(request.body)
        serializer = serializers.CountrySerializer(country, data=newData, partial=True)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
            
        return Response(status=404)


class CountriesBaseView(APIView):        
        
    def get(self, request):
        paginator = CountriesPaginator()        
        
        countries = filterCountries(request)        
        data = paginator.getpaginatedData(request, countries)
        
        serializer = serializers.CountriesSerializer(data)
        return Response(serializer.data)
        
    
    def post(self, request):
        data = json.loads(request.body)
        
        data["createdAt"] = datetime.now()
        data["groupId"] = 1
        
        serializer = serializers.CountrySerializer(data=data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(status=500)
        
        
    
        
