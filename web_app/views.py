from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from web_app.serializers import *
from web_app.models import *
from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ServidorViewSet(viewsets.ModelViewSet):
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer

class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

class VagaViewSet(viewsets.ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer

class EleicaoViewSet(viewsets.ModelViewSet):
    queryset = Eleicao.objects.all()
    serializer_class = EleicaoSerializer

class VotoViewSet(viewsets.ModelViewSet):
    queryset = Voto.objects.all()
    serializer_class = VotoSerializer

class CandidatoViewSet(viewsets.ModelViewSet):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer

def Resultado(request):
    retorno = '<h1>Resultado</h1>'
    vagas = Vaga.objects.all()
    for vaga in vagas:
        retorno += '<h3>Vaga de {}</h3>'.format(vaga.nome)
        for candidato in Candidato.objects.filter(vaga__id=vaga.id):
            retorno += '<p><strong>Candidato:</strong> {} <strong>Votos:</strong> {}</p>'.format(
                candidato.servidor.nome, len(Voto.objects.filter(candidato__id=candidato.id)))
    return HttpResponse(retorno)

