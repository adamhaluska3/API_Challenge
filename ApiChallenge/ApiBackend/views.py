from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from . import models


class CountriesIdentifiableView(APIView):
    def get(self, request, country_id):
        try:
            country = models.Country.objects.get(id = country_id)
        except models.Country.DoesNotExist:
            return Response(status=400)
        
        serializer = serializers.CountrySerializer(country)
        return Response(serializer.data)
        
        
        
# class CountriesBaseView(APIView):
    
        
