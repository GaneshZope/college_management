from django.contrib import admin
from django.urls import path 
from event import views as event_views

urlpatterns = [
    path('event/',event_views.event)
]


