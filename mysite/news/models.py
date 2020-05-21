import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)
    counts = models.IntegerField(default=0)
   
    def how_many_article(self):
        self.counts=len(Article.objects.filter(reporter=self.pk))
        return len(Article.objects.filter(reporter=self.pk))

    def __str__(self):
        return self.full_name
    how_many_article.short_description = 'Number of article'

    class Meta:
        ordering =('full_name','counts')

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

