from django.urls import path

from . import views

urlpatterns = [
    path("<int:country_id>", views.CountriesIdentifiableView.as_view(), name="yippee")
]
