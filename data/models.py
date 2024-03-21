from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=220)


class Details(models.Model):
    firstname = models.CharField(max_length=30, blank=True)
    lastname = models.CharField(max_length=30)
    username = models.EmailField()
    city  = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    zipcode = models.IntegerField()
