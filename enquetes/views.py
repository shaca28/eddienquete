from django.shortcuts import render

from .models import Pergunta


def home(request):
    ultimas_perguntas = Pergunta.objects.order_by('-data')[:5]
    contexto = {'ultimas_perguntas': ultimas_perguntas}
    return render(request, 'home.html', contexto)

def enquete(request):
    return render(request, 'enquete.html')

def detalhes(request, pergunta_id):
    pass

def resultados(request, pergunta_id):
    pass

def votos(request, pergunta_id):
    pass              
