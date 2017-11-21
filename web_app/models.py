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

class Eleicao(models.Model):
    descricao = models.CharField(max_length=128)
    dataInicio = models.DateTimeField()
    dataFim = models.DateTimeField()

    def __str__(self):
        return self.descricao 

    class Meta:
        verbose_name = 'Eleição'
        verbose_name_plural = 'Eleições'

class Vaga(models.Model):
    nome = models.CharField(max_length=50)
    eleicao = models.ForeignKey(Eleicao, null=True, blank=False)

    def __str__(self):
        return self.nome 

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'

class Token(models.Model):
    codigo = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Token'
        verbose_name_plural = 'Tokens'

class Servidor(models.Model):
    nome = models.CharField(max_length=128)
    usuario = models.ForeignKey(User, null=True, blank=False)
    votou = models.BooleanField()

    def __str__(self):
        return self.nome 

    class Meta:
        verbose_name = 'Servidor'
        verbose_name_plural = 'Servidores'

class Candidato(models.Model):
    vaga = models.ForeignKey(Vaga, null=True, blank=False)
    servidor = models.ForeignKey(Servidor, null=True, blank=False)

    def __str__(self):
        return self.servidor.nome 

    class Meta:
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'

class Voto(models.Model):
    token = models.CharField(max_length=50)
    candidato = models.ForeignKey(Candidato, null=True, blank=False)
    branco = models.BooleanField()

    class Meta:
        verbose_name = 'Voto'
        verbose_name_plural = 'Votos'