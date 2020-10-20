from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('to_confirm/', views.to_confirm, name='to_confirm'),
    path('api/confirmation/', api.api_confirmation, name='api_confirmation'),
    path('to_confirm_time/', views.to_confirm_time, name='to_confirm_time'),
]