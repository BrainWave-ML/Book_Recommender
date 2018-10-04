from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('home/',views.home),
   path('search/book/',views.display_books),
   path('populate/', views.pop_data),
]