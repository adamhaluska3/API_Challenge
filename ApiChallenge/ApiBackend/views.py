from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import json

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
        
        newData = json.loads(request.body)
        serializer = serializers.CountrySerializer(country, data=newData, partial=True)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
            
        return Response(status=404)


class CountriesBaseView(APIView):    
    def get(self, request):
        return
    
    
    def post(self, request):
        data = json.loads(request.body)
        
        data["createdAt"] = datetime.now()
        data["groupId"] = 1
        
        serializer = serializers.CountrySerializer(data=data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(status=500)
        
        
    
        
