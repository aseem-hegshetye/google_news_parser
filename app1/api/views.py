import re

import requests
from bs4 import BeautifulSoup
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app1.models import News


class GetNews(APIView):
    """
    get most recent news from first page of google news
    and store all articles as text in the db
    """
    url = 'https://news.google.com/'
    max_articles = 8  # limit number of articles to load in db

    def __init__(self, **kwargs):
        self.article_url_dict = {}
        super(GetNews, self).__init__(**kwargs)

    def get(self, request):
        """
        Delete all existing rows in News model.
        Load new articles with their names, url and content(text) into
        the db.
        """
        self.get_unique_article_urls()

        # delete all articles from News table in db
        News.objects.all().delete()

        # save all new articles to the db
        self.save_articles()

        context = {'message': 'success'}
        return Response(status=status.HTTP_200_OK, data=context)

    def get_unique_article_urls(self):
        """
        :return: scrub all article urls on self.url page
            and load unique urls along with article name
            into self.article_url_dict
        """
        content = requests.get(self.url)
        soup = BeautifulSoup(content.text, 'html.parser')
        all_links = soup.find_all('a')  # find all <a> tags
        for a in all_links:
            article_url = a.get('href')

            # if article url matches a particular format and is not none
            if article_url and re.match(r'./articles/[\w]+', article_url):
                new_url = self.url + article_url.split('./')[1]

                # only take urls that have text
                if a.text:
                    # dict will ingore duplicates
                    self.article_url_dict[new_url] = a.text

    def save_articles(self):
        """
        make get request to each article url
        and save article name, url and content as text in db
        """
        for i, a in enumerate(self.article_url_dict):

            # limit number of articles we load in db.
            if i >= self.max_articles:
                break

            response = requests.get(a)

            # only save articles that were not forbidden
            if response.status_code == 200:
                News.objects.create(
                    name=self.article_url_dict[a],
                    url=a,
                    template=response.text
                )
