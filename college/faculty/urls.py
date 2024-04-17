from django.urls import path
from faculty import views
urlpatterns=[
    path('facultyapi/',views.faultyapi,name='facultyapi')
]