from django.db import models


class News(models.Model):
    name = models.CharField(max_length=1000)
    url = models.URLField(max_length=400)
    template = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'news'
