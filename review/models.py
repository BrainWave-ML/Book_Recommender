from django.db import models
from book.models import Book

class Review(models.Model):
    title = models.TextField(max_length=100)
    body = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


    def __str__(self):
        return self.title