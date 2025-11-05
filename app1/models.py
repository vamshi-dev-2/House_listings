from django.db import models
from datetime import datetime
# Create your models here.

class House(models.Model):
    purchasing_date=models.DateField(null=True,default=None)
    registration_time=models.TimeField(null=True,default=None)
    ready_to_sale=models.BooleanField(null=False)
    name=models.CharField(max_length=25)
    owner_mail=models.EmailField(unique=False)
    price=models.FloatField()
    no_of_bedrooms=models.IntegerField()
    description=models.TextField()
    image=models.ImageField(null=True,upload_to='media/',blank=True)
    location=models.URLField()

class Owner_details(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()