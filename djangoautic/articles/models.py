# https://docs.djangoproject.com/en/2.0/ref/models/fields/
# everytime model changes, migrate
## python3 manage.py makemigrations
## python3 manage.py migrate
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    # add in author later

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + ' ...'
