from django.contrib import admin

from . import models
from .models import Article, Reporter

class ArticleAdd(admin.StackedInline):
    model = Article
    extra = 1
class ArticleAdmin(admin.ModelAdmin):
    fieldsets= [
        (None,               {'fields': ['headline']}),
        ('Date information', {'fields': ['pub_date']}),
        ('Content of news',  {'fields': ['content']}),
    ]
    
class ReporterAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,      {"fields": (['full_name']),}),
    )
    list_display = ('full_name','how_many_article')
    inlines = [ArticleAdd]

    ArticleAdmin


admin.site.register(Reporter, ReporterAdmin)