from django.urls import path
from .views import *

app_name = 'reporting_module'

urlpatterns = [
    # HTML Views
    path("", html_views.daily_report_list, name="daily_report_list"),
    path("chart/", html_views.daily_report_chart, name="daily_report_chart"),

    # API Views
    path("api/", api_views.APIDailyReportList.as_view(), name="api_daily_report_list"),
    path("api/<int:pk>/", api_views.APIDailyReportDetail.as_view(), name="api_daily_report_detail"),
]
