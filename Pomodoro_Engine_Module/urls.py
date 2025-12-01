from django.urls import path
from .views import html_views, api_views

app_name = 'pomodoro_engine_module'

urlpatterns = [
    # HTML Views
    path("", html_views.session_list, name="session_list"),
    path("create/", html_views.session_create, name="session_create"),
    path("run/<int:session_id>/", html_views.session_run, name="session_run"),
    path("start_task/<int:task_id>/", html_views.start_session_for_task, name="start_session_for_task"),
    path("update/<int:session_id>/", html_views.update_session, name="update_session"),
    path("complete/<int:pk>/", html_views.session_complete, name="session_complete"),
    path("delete/<int:session_id>/", html_views.session_delete, name="session_delete"),


    # API Views
    path("api/", api_views.APISessionList.as_view(), name="api_session_list"),
    path("api/<int:pk>/", api_views.APISessionDetail.as_view(), name="api_session_detail"),
]
