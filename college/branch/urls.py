from django.contrib import admin
from django.urls import path 
from branch import views as branch_views

urlpatterns = [
    path('branch/',branch_views.branch)
]


