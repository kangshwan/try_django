from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    # ex: /news/
    path('', views.index, name='index'),
    path('articles/', views.ArticleView.as_view(), name='article'),
    path('articles/<int:year>/', views.year_archive, name='article_year'),
    #path('articles/<int:year>/<int:month>/', views.month_archive),
    #path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]