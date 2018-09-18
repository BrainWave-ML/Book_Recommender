from django.db import models

class Store(models.Model):
    store_list = (
        ('FPK','FLIPKART'),
        ('AMZ','AMAZON'),
        ('EBY','EBAY'),
    )

    name = models.CharField(max_length=3,choices=store_list,default='NUL')
    cum_rating = models.FloatField()


    def __str__(self):
        return self.name