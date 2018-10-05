from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('home/',views.home,name='home'),
   path('',views.home),
   path('search/book/',views.display_books),
   path('register/', views.register, name='register'),
   path('login/', views.login_user, name='login'),
   path('populate/', views.pop_data),
]