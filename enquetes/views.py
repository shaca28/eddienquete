from django.shortcuts import render


def home(request):

    enquetes = {
        1: 'Pergunta 1',
        2: 'Pergunta 2',
        3: 'Pergunta 3',
    }

    dados = {
        'nome_das_enquetes': enquetes
    }
    return render(request, 'home.html', dados)

def enquete(request):
    return render(request, 'enquete.html')
