from rest_framework import serializers
from typing import Self
from datetime import datetime

from . import models


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = "__all__"
        
class LinksSerializer(serializers.Serializer):
    next = serializers.URLField(allow_null=True, required=False)
    previous = serializers.URLField(allow_null=True, required=False)

class PaginationSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    offset = serializers.IntegerField()
    limit = serializers.IntegerField()
    
class CountriesSerializer(serializers.Serializer):
    links = LinksSerializer()
    pagination = PaginationSerializer()
    countries = CountrySerializer(many=True)