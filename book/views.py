from django.shortcuts import render
from .models import Book

def home(request):
    return render(request,'home.html')

