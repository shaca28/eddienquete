from django.urls import path 

from . import views



urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),




    path('home/', views.home, name='home'),
    path('<int:pergunta_id>/', views.detalhes, name='detalhes'),
    path('<int:pergunta_id>/resulados/', views.resultados, name='resultados'),
    path('<int:pergunta_id>/votos/', views.votos, name='votos'),
]