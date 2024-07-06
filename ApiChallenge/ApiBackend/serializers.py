from rest_framework import serializers
from typing import Self
from datetime import datetime

from . import models

class CountryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CountryCreate
        fields = "__all__"

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = "__all__"

                
        