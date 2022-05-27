from django.shortcuts import render
from datetime import datetime
#from django.http import HttpResponse

from .models import Article, Category

# Create your views here.

def homepage(request):
    return render(request, "articles/homepage.html", {
        "d": datetime.now(),
        "categories": Category.objects.filter(),
        "articles": Article.objects.filter()
    })

#def homepage(request):
#    return HttpResponse("hurra! dziala")

def category(request, category_slug):
    c = Category.objects.get(slug=category_slug)
    return render(request, "articles/category.html", {
        "d": datetime.now(),
        "categories": Category.objects.filter(),
        "category": c,
        "articles": Article.objects.filter(category=c)
    })
