from django.urls import path

from . import views

urlpatterns = [
    path("countries", views.CountriesBaseView.as_view(), name=views.CountriesBaseView.__name__),
    path("countries/<int:country_id>", views.CountriesIdentifiableView.as_view(), name=views.CountriesIdentifiableView.__name__)
]
