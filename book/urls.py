from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('home/',views.home,name='home'),
   path('',views.home),
   path('search/book/',views.display_books, name='search'),
   path('compare/<int:id1>/<int:id2>/',views.compare_books, name='compare'),
   path('register/', views.register, name='register'),
   path('login/', views.login_user, name='login'),
   path('populate/', views.pop_data),
   path('product/<int:id>', views.product),
]