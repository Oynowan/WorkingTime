from django.urls import path

from . import views
from . import api

urlpatterns = [
    path('download/wt_logs/<int:pk>/', views.wt_logs, name='wt_logs'),
    path('download/u_logs/<int:pk>/', views.u_logs, name='u_logs'),
    #
    # API
    path('api/change_logs/', api.api_workingtime_change_logs, name='api_workingtime_change_logs'),
    #
    # Daily Logs
    path('daily/', views.daily_logs, name='daily'),
    #
    # Weekly Logs
    path('kw/', views.weekly_logs, name='kw'),
]
