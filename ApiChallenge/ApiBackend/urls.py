from django.urls import path

from . import views

urlpatterns = [
    path("countries", views.CountriesBaseView.as_view(), name="countries-base"),
    path("countries/<int:country_id>", views.CountriesIdentifiableView.as_view(), name="countries-identifiable")
]
