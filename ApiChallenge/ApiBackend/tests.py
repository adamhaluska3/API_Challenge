from django.test import TestCase
from rest_framework import status

from .models import Country
from .serializers import CountrySerializer


def setupDatabase(self):
    """
    Loads sample database for testing purposes.
    """
    
    self.czechia = Country.objects.create(id=1, name="Czech Republic", countryCode="CZ", createdAt="2024-01-15T08:45:30Z", groupId=101)
    self.germany = Country.objects.create(id=2, name="Germany", countryCode="DE", createdAt="2024-02-20T14:22:10Z", groupId=101)
    self.france = Country.objects.create(id=3, name="France", countryCode="FR", createdAt="2024-03-10T12:35:50Z", groupId=101)
    self.spain = Country.objects.create(id=4, name="Spain", countryCode="ES", createdAt="2024-04-05T09:40:20Z", groupId=101)
    self.italy = Country.objects.create(id=5, name="Italy", countryCode="IT", createdAt="2024-05-25T11:55:40Z", groupId=101)


class CountriesIdentifiableTests(TestCase):
    """
    Tests for "/countries/<id>" endpoint.
    """
    
    def setUp(self):
        setupDatabase(self)
    
    # GET
    def test_get_country(self):
        getRequest = self.client.get("/countries/2")
        
        self.assertEqual(getRequest.status_code, status.HTTP_200_OK)
        self.assertEqual(getRequest.data, CountrySerializer(self.germany).data)
    
    def test_get_country_invalid(self):
        getRequest = self.client.get("/countries/42")
        
        self.assertEqual(getRequest.status_code, status.HTTP_404_NOT_FOUND)
    
    # PUT
    def test_update_country(self):
        putRequest = self.client.put("/countries/3", {"name": "Hungary", "countryCode": "HU"}, content_type="application/json")
        
        self.assertEqual(putRequest.status_code, status.HTTP_200_OK)
        self.assertEqual(putRequest.data["id"], 3)
        self.assertEqual(putRequest.data["name"], "Hungary")
        
        getRequset = self.client.get("/countries/3")
        self.assertEqual(getRequset.status_code, status.HTTP_200_OK)
        self.assertEqual(getRequset.data["name"], "Hungary")
        self.assertEqual(getRequset.data["countryCode"], "HU")
        
        
class CountriesGeneralTests(TestCase):
    """
    Tests for "/countries" endpoint.
    """
    
    def setUp(self):
        setupDatabase(self)
    
    # GET
    def test_get_countries(self):
        getRequest = self.client.get("/countries")
        
        self.assertEqual(getRequest.status_code, status.HTTP_200_OK)
        self.assertEqual(getRequest.data["pagination"]["count"], 5)
        self.assertEqual(getRequest.data["pagination"]["offset"], 0)
        self.assertEqual(getRequest.data["pagination"]["limit"], 50)
        
        self.assertEqual(getRequest.data["countries"][2]["id"], 3)

    def test_get_countries_filter(self):
        getRequest = self.client.get("/countries", {"CountryCodeFiltr": "CZ", "PageLimit": "10"})
        
        self.assertEqual(getRequest.status_code, status.HTTP_200_OK)
        self.assertEqual(getRequest.data["pagination"]["count"], 1)
        self.assertEqual(getRequest.data["pagination"]["offset"], 0)
        self.assertEqual(getRequest.data["pagination"]["limit"], 10)

        self.assertEqual(getRequest.data["countries"][0], CountrySerializer(self.czechia).data)
    
    def test_get_countries_offset_invalid(self):
        getRequest = self.client.get("/countries", {"PageOffset": "12", "PageLimit": "10"})
        
        self.assertEqual(getRequest.status_code, status.HTTP_200_OK)
        self.assertEqual(getRequest.data["pagination"]["count"], 5)
        self.assertEqual(getRequest.data["pagination"]["offset"], 12)
        self.assertEqual(getRequest.data["pagination"]["limit"], 10)

        self.assertEqual(len(getRequest.data["countries"]), 0)
        
    # POST
    def test_create_country(self):
        postRequest = self.client.post("/countries", {"name": "Poland", "countryCode": "PL"}, content_type="application/json")
        
        self.assertEqual(postRequest.status_code, status.HTTP_201_CREATED)
        self.assertEqual(postRequest.data["id"], 6)
        
        getRequest = self.client.get("/countries")
        
        self.assertEqual(getRequest.data["pagination"]["count"], 6)
        self.assertEqual(getRequest.data["countries"][5]["name"], "Poland")
        
