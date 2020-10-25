from django.urls import path, include
from django.contrib.auth import views as views_
from . import views
from . import api

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views_.LogoutView.as_view(), name='logout'),
    path('login/', views_.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('users_list/', views.SearchResultView.as_view(template_name='core/list_of_users.html'), name='list_of_users'),

    # API
    path('api/get_not_confirmed_number/', api.api_get_not_confirmed_yet, name='api_get_not_confirmed_yet'),
    path('api/get_not_confirmed_time/', api.api_get_not_confirmed_time, name='api_get_not_confirmed_time'),

]