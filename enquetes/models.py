import datetime

from django.db import models
from django.utils import timezone



class Pergunta(models.Model):
    texto = models.CharField(max_length=200)
    data = models.DateTimeField('Data publicação')

    def __str__(self):
        return self.texto

class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    alternativas = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.alternativas

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)        