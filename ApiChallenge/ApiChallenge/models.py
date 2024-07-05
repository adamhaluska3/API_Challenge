from typing import str, List
from django.db import models

""" Database models"""
class Country(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    createdAt = models.DateTimeField()
    groupId = models.IntegerField()  # TODO: Ask for explanation of usage
    
    countryCreated = models.ForeignKey(on_delete=models.CASCADE)
    
    REQUIRED_FIELDS = ["id", "groupId"]


class CountryCreated(models.Model):
    name = models.CharField()
    countryCode = models.CharField()
    
    REQUIRED_FIELDS = ["name", "countryCode"]
    

""" Utility models """
class Links:
    def __init__(self, previous: str, next: str) -> None:
        self.previous = previous
        self.next = next
    
class Pagination:
    def __init__(self, count: int, offset: int, limit: int) -> None:
        self.count = count
        self.offset = offset
        self.limit = limit
    
class CollectionResult:
    def __init__(self, links: Links, pagination: Pagination) -> None:
        self.links = links
        self.pagination = pagination
        
class Countries:
    def __init__(self, collectionResult: CollectionResult, countries: List[Country]) -> None:
        self.collectionResult = collectionResult
        self.countries = countries
