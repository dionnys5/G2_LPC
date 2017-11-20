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
        fields = ('username','email','is_staff', 'url')

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UserSerializer(many=False)
    class Meta:
        model = Pessoa
        fields = '__all__'
        
    def create(self, data):
        usuario = data.pop('usuario')
        user = User.objects.create(**usuario)
        pessoa = Pessoa.objects.create(usuario=user, **data)
        return pessoa
    
    def update(self, pessoa, data):
        pessoa.nome = data.get('nome', pessoa.nome)
        pessoa.idade = data.get('idade', pessoa.idade)
        pessoa.cpf = data.get('cpf', pessoa.cpf)
        pessoa.save()
        return pessoa

