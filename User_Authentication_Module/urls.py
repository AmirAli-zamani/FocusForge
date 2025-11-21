from django.urls import path
from .views import api_views, html_views

app_name = 'user_authentication_module'

urlpatterns = [
    # Landing Page
    path("", html_views.landing_view, name="landing"),
    
    # HTML Views
    path('register/', html_views.register_view, name='register'),
    path('login/', html_views.login_view, name='login'),
    path('logout/', html_views.logout_view, name='logout'),
    path('profile/', html_views.profile_view, name='profile'),
    path('profile/update/', html_views.profile_update_view, name='profile_update'),

    # API Views
    path('api/register/', api_views.APIRegisterView.as_view(), name='api_register'),
    path('api/login/', api_views.APILoginView.as_view(), name='api_login'),
    path('api/profile/', api_views.APIProfileView.as_view(), name='api_profile'),
]
