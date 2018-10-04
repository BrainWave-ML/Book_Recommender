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
    review_value = models.IntegerField(null=True,blank=True,default=0)
    price = models.FloatField()
    sale = models.IntegerField()
    year = models.IntegerField(null=True,blank=True,default=1994)
    image = models.TextField(default='/static/default_book.gif')
    delivery_time = models.IntegerField(default=4)
    url = models.URLField(null=True,blank=True)
    genre = models.CharField(max_length=3,choices=genre_list,default='NULL')
    ISBN = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    modified_at = models.DateTimeField(auto_now=True,editable=False)

    def __str__(self):
        return self.name+'-'+self.store.name