from django.urls import path
from . import views


urlpatterns = [

    path('api/', views.api_root),
    path('api/workingtime/', views.WorkingTimeList.as_view(), name='workingtime-list'),
    path('api/workingtime/<int:pk>/', views.WorkingTimeDetail.as_view(), name='workingtime-detail'),
    path('api/userprofile/', views.UserProfileList.as_view(), name='userprofile-list'),
    path('api/userprofile/<int:pk>/', views.UserProfileDetail.as_view(), name='userprofile-detail')

]