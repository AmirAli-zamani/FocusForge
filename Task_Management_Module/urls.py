from django.urls import path
from .views import *

app_name = 'task_manager'

urlpatterns = [
    # HTML
    path("", task_list, name="task_list"),
    path("create/", task_create, name="task_create"),
    path("<int:task_id>/edit/", task_edit, name="task_edit"),
    path("<int:task_id>/delete/", task_delete, name="task_delete"),

    # API
    path("api/", APITaskList.as_view(), name="api_task_list"),
    path("api/<int:pk>/", APITaskDetail.as_view(), name="api_task_detail"),
]
