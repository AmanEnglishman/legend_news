from django.shortcuts import render

from .models import News

def home(request):
    news = News.objects.order_by('-created_at')
    return render(request, 'home_page.html', {'news': news})

def contacts(request):
    return render(request, 'contacts.html')

