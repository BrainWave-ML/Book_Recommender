from django.db import models
from store.models import Store

class Book(models.Model):
    
    genre_list = (
        ('FCN','Fiction'),
        ('ABG','Autobiography'),
    )
    name = models.TextField(max_length=50)
    author = models.TextField(max_length=30)
    rating = models.FloatField()
    store = models.ForeignKey(Store,on_delete=models.CASCADE)
    review_value = models.IntegerField()
    price = models.FloatField()
    sale = models.IntegerField()
    year = models.IntegerField()
    genre = models.CharField(max_length=3,choices=genre_list,default='NUL')
    ISBN = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    modified_at = models.DateTimeField(auto_now=True,editable=False)

    def __str__(self):
        return self.name+'-'+self.store.name