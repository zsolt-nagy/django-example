from django.db import models
import datetime

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateField(default=datetime.date.today)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    stock = models.IntegerField(default=0)

    def buy_book(self):
        self.stock -= 1
        self.save()        
