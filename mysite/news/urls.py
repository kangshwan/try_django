from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    # ex: /news/
    path('', views.index, name='index'),
    path('articles/', views.ArticleView.as_view(), name='articles'),
    path('articles/<int:year>/', views.year_archive, name='article_year'),
    #path('artricles/<int:pk>/', views.ContentView.as_view(), name='content'),
    path('articles/<int:year>/<int:month>/', views.month_archive, name='article_month'),
    path('articles/<int:year>/<int:month>/<int:pk>/', views.ContentView.as_view(), name='content'),
]