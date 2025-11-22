from django.urls import path
from .views import landing_view

app_name = 'Landing'

urlpatterns = [
    path("", landing_view, name='Landing'),
]
