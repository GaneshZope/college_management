from django.urls import path
from department import views

urlpatterns=[
    path('deptapi/',views.departmentapi,name='deptapi')
    ]