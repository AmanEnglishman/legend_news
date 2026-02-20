from django.db.models import F
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .models import News, Category
from .forms import ContactForm

def home(request):
    news = News.objects.order_by('-created_at')
    return render(request, 'home_page.html', {'news': news})

def contacts(request):
    success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

        full_message = f'''
Новое сообщение от сайта Legend News

Имя - {name}
Email - {email}

Сообщение: 
{message} 
'''
        send_mail(
            subject='Legend News',
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['englishmanaman@gmail.com'],
            fail_silently=False,
        )

        success = True
        form = ContactForm()

    else:
        form = ContactForm()

    return render(request, 'contacts.html', {'form': form, 'success': success})

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
