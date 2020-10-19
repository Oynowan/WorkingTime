from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('to_confirm/', views.to_confirm, name='to_confirm'),
    path('to_confirm/api/confirmation', api.api_confirmation, name='api_confirmation'),
    path('to_confirm_time/', views.to_confirm_time, name='to_confirm_time'),
    path('to_confirm_time/api/confirm_time', api.api_confirm_time, name='api_confirm_time'),
    path('correcting_time/<int:time_id>', views.correcting_time, name='correcting_time'),
    path('correcting_time/<int:time_id>/api/confirm_time', api.api_confirm_time, name='api_confirm_time'),
]