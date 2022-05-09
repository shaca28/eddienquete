from django.contrib import admin

from .models import Pergunta, Resposta

class ListandoPergunta(admin.ModelAdmin):
    list_display = ('id', 'texto', 'data')
    list_display_links = ('id', 'texto', 'data')
    search_fields = ('texto',)
    list_filter = ('texto',)
    list_per_page = 6

class ListandoResposta(admin.ModelAdmin):
    list_display = ('id', 'pergunta', 'votos')
    list_display_links = ('id', 'pergunta', 'votos')
    search_fields = ('pergunta',)
    list_filter = ('pergunta',)


admin.site.register(Pergunta, ListandoPergunta)
admin.site.register(Resposta, ListandoResposta)