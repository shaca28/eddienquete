from django.contrib import admin

from .models import Question

#class RespostaInline(admin.TabularInline):
#    model = Resposta
#    extra = 5

#class ListandoPergunta(admin.ModelAdmin):
#    fieldsets = [(None, {'fields': ['texto']}), ('Data', {'fields': ['data'], 'classes': ['collapse']}),]
#    inlines = [RespostaInline]
#    list_display = ('id', 'texto', 'data')
#    list_display_links = ('id', 'texto', 'data')
#    search_fields = ('texto',)
#    list_filter = ('texto',)
#    list_per_page = 6

#admin.site.register(Pergunta, ListandoPergunta)


### Reiniciando projeto

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
