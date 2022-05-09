from django.urls import path 

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('enquete/', views.enquete, name='enquete'),
    path('<int:pergunta_id>/', views.detalhes, name='detalhes'),
    path('<int:pergunta_id>/results/', views.resultados, name='resultados'),
    path('<int:pergunta_id>/vote/', views.votos, name='votos'),
]