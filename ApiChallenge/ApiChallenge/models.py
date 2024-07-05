from typing import str, List, Self
from django.db import models

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

        
class CountryCreated:
    def __init__(self, name: str, countryCode: str) -> None:
        self.name = name
        self.countryCode = countryCode
        
class Countries:
    def __init__(self, collectionResult: CollectionResult, countries: List[Country]) -> None:
        self.collectionResult = collectionResult
        self.countries = countries

   
   
""" Database models""" 
class Country(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    createdAt = models.DateTimeField()
    groupId = models.IntegerField()  # TODO: Ask for explanation of usage
    
    name = models.CharField()
    countryCode = models.CharField()
    
    REQUIRED_FIELDS = ["id", "groupId"]
