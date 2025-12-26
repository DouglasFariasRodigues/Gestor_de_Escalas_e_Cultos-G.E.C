import random
from django.db.models import Q

import escala
from .models import Obreiro,Local,NatCulto,Culto,Escala,EscalaItem,Indisponibilidade


#Criação da escala
def gerar_escala_Automaticamente(mes, ano):
    escala, created = Escala.objects.get_or_create(
        mes=mes, 
        ano=ano, 
        defaults={'status': Escala.Status.RASCUNHO}
    )

    #busca de cultos do mês e ano informados
    cultos = Culto.objects.filter(data_hora__year=ano, data_hora__month=mes)

    obreiros = Obreiro.objects.filter(ativo = True)

    itens_gerados = 0 


    #verificação de cada culto para não haver duplicação de escalados
    for culto in cultos:
        if EscalaItem.objects.filter(escala=escala, culto=culto).exists():
            continue

        obreiros_disponiveis = []

        for obreiro in obreiros:
            esta_indisponivel = Indisponibilidade.objects.filter(obreiro = obreiro, data_inicio__lte = culto.data_hora, data_fim__gte = culto.data_hora).exists()

            if not esta_indisponivel:
                obreiros_disponiveis.append(obreiro)
            
        if obreiros_disponiveis:
            escolhido = random.choice(obreiros_disponiveis)
            EscalaItem.objects.create(escala=escala,culto=culto,obreiro=escolhido)
            itens_gerados +=1
    return f'Processo concluído. {itens_gerados} itens de escala foram gerados.'