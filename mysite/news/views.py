import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views import generic
from django.template import loader

from .models import Article

def index(request):
    latest_article_list=Article.objects.all()
    template= loader.get_template('news/index.html')
    context={
        'latest_article_list': latest_article_list,
    }
    return HttpResponse(template.render(context, request))

class IndexView(generic.ListView):
    template_name='news/index.html'
    context_object_name='latest_article_list'
    

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)    

class ArticleView(generic.ListView):
    template_name='news/article.html'
    context_object_name='latest_article_list'
    def get_queryset(self):
        return Article.objects.filter(pub_date__lte=datetime.date.today()).order_by('-pub_date')[:5]
