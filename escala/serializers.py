from rest_framework import serializers
from .models import Obreiro,Local,NatCulto,Culto,Escala,EscalaItem

class ObreiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obreiro
        fields = '__all__'

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = '__all__'

class NatCultoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NatCulto
        fields = '__all__'

class CultoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Culto
        fields = '__all__'

class EscalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escala
        fields = '__all__'
    

class EscalaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EscalaItem
        fields = '__all__'
