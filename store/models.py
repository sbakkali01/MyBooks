from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)

class Product(models.Model):
    title=models.CharField(max_length=200)
    category=models.ForeignKey(to="Category",on_delete=models.CASCADE)
    created_by=models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description=models.TextField(max_length=2000)
    image=models.ImageField()
