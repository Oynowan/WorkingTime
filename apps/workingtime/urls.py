from django.urls import path
from . import views

urlpatterns = [

    path('working/', views.working, name='working'),

]
