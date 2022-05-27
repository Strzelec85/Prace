from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField()

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

