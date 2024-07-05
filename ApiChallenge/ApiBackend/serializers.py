from rest_framework import serializers
from typing import Self
from datetime import datetime

from . import models


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = "_all__"
    
    def createCountry(self, countryCreated: models.CountryCreated, 
                      countryId: int, groupId: int) -> Self:
        newCountry = models.Country.objects.create(id = countryId,
                                            createdAt = datetime.now(),
                                            groupId = groupId,
                                            name = countryCreated.name,
                                            countryCode = countryCreated.countryCode)
        newCountry.save()
        return newCountry

                
        