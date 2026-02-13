from django.urls import path

from .views import home, contacts, news_list
urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('news_list/', news_list, name='news_list'),


]