from django.urls import include, path

from app1.views import *

app_name = 'app1'
urlpatterns = [
    path('api/', include('app1.api.urls')),
    path('', NewsListView.as_view(), name='news_list'),
    path('article/<pk>/', NewsDetailView.as_view(), name='news_detail')
]
