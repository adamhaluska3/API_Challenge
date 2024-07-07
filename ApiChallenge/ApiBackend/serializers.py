from rest_framework import serializers
from typing import Self
from datetime import datetime

from . import models


class CountrySerializer(serializers.ModelSerializer):
    """
    Serializer for Country model.
    
    Fields:
        Same as 'Country' model.
    """
    class Meta:
        model = models.Country
        fields = "__all__"
        
class LinksSerializer(serializers.Serializer):
    """
    Serializer for a Links object.

    Fields:
        next (URL): URL address (GET request) for following entries.
        previous (URL): URL address (GET request) for previous entries.
    """
    next = serializers.URLField(allow_null=True, required=False)
    previous = serializers.URLField(allow_null=True, required=False)

class PaginationSerializer(serializers.Serializer):
    """
    Serializer for a Pagination object.

    Fields:
        count (int): Total number of suitable entries.
        offset (int): Index of a first entry in a HTTP response.
        limit (int): Maximal number of entries in a HTTP response.
    """
    count = serializers.IntegerField()
    offset = serializers.IntegerField()
    limit = serializers.IntegerField()
    
class CountriesSerializer(serializers.Serializer):
    """
    Serializer for a Countries object.

    Fields:
        links (Links): Object with URL addresses for retrieving previous/next list of Countries.
        pagination (Pagination): Object with data of total amount, starting index 
                                 and amount of returned countries.
        countries (List[Country]): List of countries.
    """
    links = LinksSerializer()
    pagination = PaginationSerializer()
    countries = CountrySerializer(many=True)