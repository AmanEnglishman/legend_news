from django.urls import path

from .views import home, contacts, news_detail, categories, categories_news
urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:news_id>/', news_detail, name='news_detail'),
    path('categories/', categories, name='categories'),
    path('categories/<int:category_id>/', categories_news, name='categories_news'),
]