from django.db import models
from django.contrib.auth.models import User

'''
principais models

models.CharField(max_length=128)
models.TextField()
models.IntegerField()
models.ForeignKey(Pessoa, null=True, blank=False)
models.DateTimeField()
models.TimeField()
models.CharField(max_length=50, choices=[('publica', 'publica')], default='publica')
'''



class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    idade = models.CharField(max_length=3)
    cpf = models.CharField(max_length=11)
    usuario = models.ForeignKey(User, null=True, blank=False)

    def __str__(self):
        return self.nome 

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
