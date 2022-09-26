from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    price = models.IntegerField()
    description = models.CharField(max_length=2000)
    address = models.CharField(max_length=1000)
    is_published = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=250)
