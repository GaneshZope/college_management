from django.contrib import admin
from django.urls import path 
from student import views as student_views

urlpatterns = [
    path('student/',student_views.student)
]


