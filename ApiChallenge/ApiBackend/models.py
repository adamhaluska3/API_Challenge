from typing import List, Self
from django.db import models

""" Database models""" 
class Country(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    createdAt = models.DateTimeField()
    groupId = models.IntegerField()  # TODO: Ask for explanation of usage
    
    #CountryCreated parameters
    name = models.CharField(max_length=64)
    countryCode = models.CharField(max_length=16)
    
    REQUIRED_FIELDS = ["id", "groupId"]
