from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'price', 'store', 'year']
    list_filter = ('store', 'year') 

admin.site.register(Book, BookAdmin)