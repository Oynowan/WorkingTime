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

urlpatterns = [
    #
    # Core app
    path('', include('apps.core.urls')),
    #
    # WorkingTime APP
    path('', include('apps.workingtime.urls')),
    #
    # Tips APP
    path('', include('apps.tips.urls')),
    #
    # Confirmations APP
    path('', include('apps.confirmations.urls')),
    #
    # UserProfile
    path('', include('apps.userprofile.urls')),
    #
    # Admin
    path('new_path/for/admin/', admin.site.urls),
    #
    # DRF Api
    path('', include('apps.drf.urls')),
]
