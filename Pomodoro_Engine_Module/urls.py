from django.urls import path
from .views import *

app_name = 'pomodoro_engine_module'

urlpatterns = [
    # HTML Views
    path("", html_views.session_list, name="session_list"),
    path("create/", html_views.session_create, name="session_create"),

    # API Views
    path("api/", api_views.APISessionList.as_view(), name="api_session_list"),
    path("api/<int:pk>/", api_views.APISessionDetail.as_view(), name="api_session_detail"),
]
