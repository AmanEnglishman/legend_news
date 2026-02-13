from django.db.models import F
from django.shortcuts import render

from .models import News

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