from django.contrib import admin
from django.urls import path
from . import views
app_name='base'
urlpatterns = [
    path('',views.edit,name='edit'),
]