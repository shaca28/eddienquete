from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def enquete(request):
    return render(request, 'enquete.html')
