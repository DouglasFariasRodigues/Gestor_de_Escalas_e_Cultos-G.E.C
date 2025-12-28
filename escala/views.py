from rest_framework import viewsets
from .models import Obreiro,Local,NatCulto,Culto,Escala,EscalaItem,Indisponibilidade
from .serializers import (ObreiroSerializer,LocalSerializer,NatCultoSerializer,CultoSerializer,EscalaSerializer,EscalaItemSerializer,IndisponibilidadeSerializer)

class ObreirosViewSet(viewsets.ModelViewSet):
    queryset = Obreiro.objects.all().order_by('nome')
    serializer_class = ObreiroSerializer

class Local_ViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all().order_by('nome')
    serializer_class = LocalSerializer
    
class NatCultoViewSet(viewsets.ModelViewSet):
    queryset = NatCulto.objects.all().order_by('nome')
    serializer_class = NatCultoSerializer

class CultoViewSet(viewsets.ModelViewSet):
    queryset = Culto.objects.all().order_by('data_hora')
    serializer_class = CultoSerializer

class EscalaViewSet(viewsets.ModelViewSet):
    queryset = Escala.objects.all().order_by('ano','mes')
    serializer_class = EscalaSerializer

class EscalaItemViewSet(viewsets.ModelViewSet):
    queryset = EscalaItem.objects.all()
    serializer_class = EscalaItemSerializer

class IndisponibilidadeViewSet(viewsets.ModelViewSet):
    queryset = Indisponibilidade.objects.all().order_by('data_inicio')
    serializer_class = IndisponibilidadeSerializer
    

# Create your views here.
