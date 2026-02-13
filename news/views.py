from django.shortcuts import render

from .models import News

def home(request):
    return render(request, 'home_page.html')

def contacts(request):
    return render(request, 'contacts.html')

def news_list(request):
    news = News.objects.order_by('-created_at')
    return render(request, 'news_list.html', {'news': news})