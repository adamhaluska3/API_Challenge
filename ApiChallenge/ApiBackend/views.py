from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from json import loads

from datetime import datetime

from . import serializers
from . import models


def getCountryById(countryId: int) -> models.Country | None:
    try:
        return models.Country.objects.get(id = countryId)
    except models.Country.DoesNotExist:
        return None


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
        
        serializer = serializers.CountrySerializer(country, data=request.body, partial=True)
        outputCountryCreate = models.CountryCreate(serializer.data["name"], serializer.data["countryCode"])
        return Response(outputCountryCreate)

class CountriesBaseView(APIView):    
    def get(self, request):
        return
    
    def post(self, request):
        data = loads(request.body)
        data["createdAt"] = datetime.now()
        data["groupId"]  = 1
        
        serializer = serializers.CountrySerializer(data=data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(status=500)
        
        
    
        
