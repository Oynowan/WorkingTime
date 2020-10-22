from django.urls import path

from . import views

urlpatterns = [
    path('download/wt_logs/<int:pk>/', views.wt_logs, name='wt_logs'),
    path('download/u_logs/<int:pk>/', views.u_logs, name='u_logs'),
]
