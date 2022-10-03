from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('consultation/', views.consultation, name='consultation'),
    path('contact/', views.contact, name='contact'),
    path('process/', views.process, name='process')
]
