from rest_framework import serializers
from .models import Obreiro,Local,NatCulto,Culto,Escala,EscalaItem,Indisponibilidade

class ObreiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obreiro
        fields = ['id', 'nome', 'ativo', 'cargo']
    
    def get_escalas_no_mes(self,obj):
        request = self.context.get('request')
        if not request:
            return None
        
        try:
            mes = int(mes)
            ano = int(ano)
            
        except (ValueError, TypeError):
            return 0
        
        return obj.escalas.filter(culto_data_hora__month = mes, culto_data_hora__year = ano).count()

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