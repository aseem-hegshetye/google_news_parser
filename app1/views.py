from django.views.generic import DetailView, ListView

from app1.models import *


class NewsListView(ListView):
    template_name = 'app1/news_list.html'
    model = News


class NewsDetailView(DetailView):
    template_name = 'app1/news_detail.html'
    model = News
