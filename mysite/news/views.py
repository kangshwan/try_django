import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views import generic
from django.template import loader
from django.db.models.functions import ExtractYear
from django.db.models import Max, Count

from .models import Article

def index(request):
    article_list=Article.objects.all()
    template= loader.get_template('news/index.html')
    context={
        'article_list': article_list,
    }
    return HttpResponse(template.render(context, request))

class IndexView(generic.ListView):
    template_name='news/index.html'
    context_object_name='latest_article_list'
    

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year).order_by('pub_date')
    m_list = a_list.distinct().values('pub_date')
    context = {'year': year, 'article_list': a_list,'month_list': m_list}
    return render(request, 'news/year_archive.html', context)    

def month_archive(request, year, month):
    a_list = Article.objects.filter(pub_date__year=year, pub_date__month=month).order_by('pub_date')
    m_list = Article.objects.filter(pub_date__year=year).order_by('pub_date').distinct().values('pub_date')
    context = {'year': year, 'month': month, 'article_list': a_list,'month_list':m_list}
    return render(request, 'news/month_archive.html', context)
class ContentView(generic.DetailView):
    model = Article
    template_name='news/content.html'

class ArticleView(generic.ListView):
    template_name='news/article.html'

    duplicates = Article.objects.annotate(year=ExtractYear('pub_date'))
    def get_queryset(self):
        return Article.objects.filter(pub_date__lte=datetime.date.today()).order_by('-pub_date')[:5]
    
    def get_context_data(self, **kwargs):
        #yearlist=[]
        #for year in Article.objects.values('pub_date').distinct():
        #    yearlist.append()
        context = super(ArticleView, self).get_context_data(**kwargs)
        context['article_list'] = Article.objects.all()
        #context['year_list'] = Article.objects.values('pub_date').annotate(year_count=Count('pub_date'))
        context["year_list"] = Article.objects.all().order_by('-pub_date').distinct().values('pub_date')
        #print(context)
        return context
