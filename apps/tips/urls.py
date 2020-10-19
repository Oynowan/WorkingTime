from django.urls import path
from . import views
urlpatterns = [
    path('tips/', views.views_employees, name='views_employees'),
    path('tips/tips_shared/', views.tips_shared, name='tips_shared'),
]