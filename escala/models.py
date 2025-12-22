from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

class Obreiro(models.Model):
    nome = models.CharField(
        max_length=100,
        unique=True,
        help_text="Nome completo do obreiro."
    )
    cargo = models.CharField(
        max_length=50,
        help_text="Cargo ou função principal do obreiro na igreja."
    )
    ativo = models.BooleanField(
        default=True,
        help_text="Indica se o obreiro está ativo e pode ser escalado."
    )
 
    class Meta:
        verbose_name = "Obreiro"
        verbose_name_plural = "Obreiros"
        ordering = ['nome']
 
    def __str__(self):
        return self.nome

class Local(models.Model):
    nome = models.CharField(
        max_length=100,
        unique=True,
        help_text="Nome do local do culto (ex: Sede, Congregação A)."
    )
    ativo = models.BooleanField(
        default=True,
        help_text="Indica se o local está ativo para novos cultos."
    )
 
    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locais"
        ordering = ['nome']
 
    def __str__(self):
            return self.nome
        

class NatCulto(models.Model):
    nome = models.CharField(
        max_length=100,
        unique=True,
        help_text="Nome ou descrição da natureza do culto."
    )
    ativo = models.BooleanField(
        default=True,
        help_text="Indica se esta natureza de culto está ativa."
    )
 
    class Meta:
        verbose_name = "Natureza do Culto"
        verbose_name_plural = "Naturezas de Culto"
        ordering = ['nome']
 
    def __str__(self):
        return self.nome

class Culto(models.Model):
    """Representa um evento de culto agendado, com data, hora e local."""
    local = models.ForeignKey(Local, on_delete=models.PROTECT, related_name="cultos")
    nat_culto = models.ForeignKey(NatCulto, on_delete=models.PROTECT, related_name="cultos")
    data_hora = models.DateTimeField(help_text="Data e hora de início do culto.")
 
    class Meta:
        verbose_name = "Culto"
        verbose_name_plural = "Cultos"
        ordering = ['data_hora']
        # Garante que não haja dois cultos no mesmo local e horário
        unique_together = ('local', 'data_hora')
 
    def __str__(self):
        data_formatada = self.data_hora.strftime('%d/%m/%Y às %H:%M')
        return f"{self.nat_culto} em {self.local} - {data_formatada}"

class Escala(models.Model):
    mes = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)],
        help_text="Mês da escala (1 a 12)."
    )
    ano = models.IntegerField(help_text="Ano da escala (ex: 2024).")
    status = models.CharField(
        max_length=20,
        default='Rascunho',
        help_text="Estado atual da escala (ex: Rascunho, Publicada)."
    )

    class Meta:
        verbose_name = "Escala Mensal"
        verbose_name_plural = "Escalas Mensais"
        unique_together = ('mes', 'ano') # Garante apenas uma escala por mês/ano

    def __str__(self):
        return f"Escala {self.mes}/{self.ano} - {self.status}"

class EscalaItem(models.Model):
    """Item da escala que associa um obreiro a um culto específico."""
    escala = models.ForeignKey(Escala, on_delete=models.CASCADE, related_name="itens")
    culto = models.ForeignKey(Culto, on_delete=models.CASCADE, related_name="itens_escala")
    obreiro = models.ForeignKey(Obreiro, on_delete=models.PROTECT, related_name="escalas")
 
    class Meta:
        verbose_name = "Item da Escala"
        verbose_name_plural = "Itens da Escala"
        # Garante que um obreiro não seja escalado duas vezes para o mesmo culto
        unique_together = ('culto', 'obreiro')
 
    def __str__(self):
        return f"{self.obreiro.nome} escalado para {self.culto}"