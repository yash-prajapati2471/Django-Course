from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('forms',views.forms,name='forms'),
    path('login',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
]