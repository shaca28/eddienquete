from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Pergunta, Resposta


def home(request):
    ultimas_perguntas = Pergunta.objects.order_by('-data')[:5]
    contexto = {'ultimas_perguntas': ultimas_perguntas}
    return render(request, 'home.html', contexto)

def enquete(request):
    return render(request, 'enquete.html')

def detalhes(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request, 'detalhes.html', {'pergunta': pergunta})     

def resultados(request, pergunta_id):
    pass

def votos(request, pergunta_id):
    pass
