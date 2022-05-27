from django.contrib import admin

# Register your models here.

from .models import Article
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug'
    )

class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug'
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)


