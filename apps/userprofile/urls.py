from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('profile/<str:user>/', views.user_profile_ui, name='user_profile_ui'),
    path('api/save_profile_changes/', api.api_save_profile_changes, name='api_save_profile_changes'),
]