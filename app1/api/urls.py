from django.urls import path

from app1.api.views import *

app_name = 'api'
urlpatterns = [
    path('get_news/', GetNews.as_view(), name='get_news'),
]
