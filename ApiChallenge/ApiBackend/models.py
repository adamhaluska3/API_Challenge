from typing import List, Self
from django.db import models

class Country(models.Model):
    """
    Model for storing data of a country.
    
    Fields:
        id (int): ID of an entry (auto-generated, read-only).
        createdAt (str): Timestamp of request for creation.
        groupId (int): TODO
        name (str): Name of a country.
        countryCode (str): Code of a country.
    """
    id = models.AutoField(primary_key=True, editable=False)
    createdAt = models.DateTimeField()
    groupId = models.IntegerField()  # TODO: Ask for explanation of usage
    
    # CountryCreated parameters
    name = models.CharField(max_length=64)
    countryCode = models.CharField(max_length=16)
