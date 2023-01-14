# myapp/models.py
from django.db import models

class PortfolioItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_items')

# myapp/views.py
from django.shortcuts import render
from .models import PortfolioItem

def portfolio_view(request):
    items = PortfolioItem.objects.all()
    return render(request, 'portfolio.html', {'items': items})

# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('portfolio/', views.portfolio_view, name='portfolio'),
]

# myapp/templates/portfolio.html
{% for item in items %}
    <h2>{{ item.title }}</h2>
    <p>{{ item.description }}</p>
    <img src="{{ item.image.url }}" alt="{{ item.title }}">
{% endfor %}