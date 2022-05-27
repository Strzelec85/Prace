from django.urls import path
from .views import homepage, category

urlpatterns = [
    path('', homepage),
    path('category/<slug:category_slug>', category, name='category')
]
