from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    inlines = [ChoiceInline]
    
admin.site.register(Question, QuestionAdmin)
=======
from .models import Question

admin.site.register(Question)
>>>>>>> 7ceb300ffff9647f444a160801aae05cfa7e146d
