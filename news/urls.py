from django.urls import path

from .views import home, contacts, news_detail
urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:news_id>/', news_detail, name='news_detail'),
]