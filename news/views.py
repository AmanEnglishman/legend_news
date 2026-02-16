from django.db.models import F
from django.shortcuts import render

from .models import News, Category


def home(request):
    news = News.objects.order_by('-created_at')
    return render(request, 'home_page.html', {'news': news})

def contacts(request):
    return render(request, 'contacts.html')

def news_detail(request, news_id):
    news = News.objects.get(id=news_id)
    News.objects.filter(id=news_id).update(views=F('views') + 1)
    news.refresh_from_db()
    return render(request, 'news_detail.html', {'news': news})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def categories_news(request, category_id):
    news = News.objects.filter(category_id=category_id)
    return render(request, 'categories_news.html', {'news': news})