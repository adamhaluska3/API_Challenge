from rest_framework import serializers
from typing import Self
from datetime import datetime

from . import models


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = "__all__"
    
    def createCountry(self, countryCreate: models.CountryCreate, 
                      countryId: int, groupId: int) -> Self:
        newCountry = models.Country.objects.create(id = countryId,
                                            createdAt = datetime.now(),
                                            groupId = groupId,
                                            name = countryCreate.name,
                                            countryCode = countryCreate.countryCode)
        newCountry.save()
        return newCountry

                
        