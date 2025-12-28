from rest_framework import serializers
from .models import Obreiro,Local,NatCulto,Culto,Escala,EscalaItem,Indisponibilidade

class ObreiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obreiro
        fields = ['id', 'nome', 'ativo', 'cargo']

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ['id', 'nome', 'ativo']

class NatCultoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NatCulto
        fields = ['id', 'nome', 'ativo']

class CultoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Culto
        fields = ['id', 'local', 'nat_culto', 'data_hora']

class EscalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escala
        fields = ['id', 'mes', 'ano', 'status']
    

class EscalaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EscalaItem
        fields = ['id', 'escala', 'culto', 'obreiro']

class IndisponibilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indisponibilidade
        fields = ['id', 'obreiro', 'data_inicio', 'data_fim','motivo']