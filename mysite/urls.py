"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # User Authentication
    path("auth/", include("User_Authentication_Module.urls")),

    # Task Management
    path("tasks/", include("Task_Management_Module.urls")),

    # Pomodoro Engine
    path("pomodoro/", include("Pomodoro_Engine_Module.urls")),

    # Reporting
    path("reports/", include("Reporting_Module.urls")),

    #Landing
    path("", include("Landing.urls"))
]
