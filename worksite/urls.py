"""worksite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.urls import include
from django.contrib.auth import views

from apps.core.views import frontpage, signup, delete_workingtime
from apps.workingtime.views import working, start_working, end_working, working_2
from apps.tips.views import views_employees, tips_shared
from apps.workingtime.api import api_start_working, api_end_working

urlpatterns = [

    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('deleted/', delete_workingtime, name='delete_workingtime'),


    path('working/', working, name='working'),
    #path('working_2/', working_2, name='working_2'),
    path('workingtime/start_working/', start_working, name='start_working'),
    path('workingtime/end_working/', end_working, name='end_working'),

    #
    # API

    #path('api/start_working/', api_start_working, name='api_start_working'),
    #path('api/end_working/', api_end_working, name='api_end_working'),


    path('tips/', views_employees, name='views_employees'),
    path('tips/tips_shared/', tips_shared, name='tips_shared'),

    path('admin/', admin.site.urls),
]
