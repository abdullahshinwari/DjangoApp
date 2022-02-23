from django.db import models

# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)


class Articles(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
