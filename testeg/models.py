import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Category(models.Model):
    title = models.CharField(max_length=10)
    slug = models.SlugField()

    def __str__(self):
        return self.title

class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=255, db_index=True, default='')
    price = models.IntegerField(blank=True, null=True)
    detail_text = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='productss', on_delete=models.CASCADE)
    published_date = models.DateTimeField(blank=True, null=True)
    published=models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
