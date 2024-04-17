from django.urls import path
from collge import views

urlpatterns={
    path('collageapi/',views.collageapi,name='col_api'),
}