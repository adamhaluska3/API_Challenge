from django.urls import path

from . import views

urlpatterns = [
    path("", views.CountriesBaseView.as_view(), name=views.CountriesBaseView.__name__),
    path("<int:country_id>", views.CountriesIdentifiableView.as_view(), name=views.CountriesIdentifiableView.__name__)
]
