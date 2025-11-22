from django.urls import path
from .views import html_views , api_views

app_name = "task_management_module"

urlpatterns = [
    # HTML
    path("", html_views.task_list, name="task_list"),
    path("create/", html_views.task_create, name="task_create"), 
    path("<int:task_id>/edit/", html_views.task_edit, name="task_edit"),
    path("<int:task_id>/delete/", html_views.task_delete, name="task_delete"),

    # API
    path("api/", api_views.APITaskList.as_view(), name="api_task_list"),
    path("api/<int:pk>/", api_views.APITaskDetail.as_view(), name="api_task_detail"),
]
