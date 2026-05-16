from django.db import models

# Create your models here.

class Coffee(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)
