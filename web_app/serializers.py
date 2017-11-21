from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from web_app.models import *

'''
Principais Campos

fields = (‘id’, ‘nome’)
fields = ‘__all__’
exclude = ('id', )
'''

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username','email')

class ServidorSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UserSerializer(many=False)
    class Meta:
        model = Servidor
        fields = ('nome','usuario','votou')
        
    def create(self, data):
        usuario = data.pop('usuario')
        user = User.objects.create(**usuario)
        servidor = Servidor.objects.create(usuario=user, **data)
        return servidor

class EleicaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eleicao
        fields = '__all__'

class VagaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vaga
        fields = '__all__'

class TokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'

class CandidatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidato
        fields = ('vaga','servidor')

class VotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Voto
        fields = '__all__'
