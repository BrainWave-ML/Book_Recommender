from django.db import models
from django.contrib.auth.models import User
from book.models import Book

class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
