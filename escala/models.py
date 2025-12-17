from django.db import models

class Obreiro(models.Model):
    nome = models.CharField(max_length = 100, unique = True)
    cargo = models.CharField(max_length = 100)
    ativo = models.BooleanField(default = True)
    def __str__(self):
        return self.nome

class Local(models.Model):
    nome = models.CharField(max_length = 100, unique = True)
    ativo = models.BooleanField(default = True)
    def __str__(self):
            return self.nome

class NatCulto(models.Model):
    nome = models.CharField(max_length = 100, unique = True)
    ativo = models.BooleanField(default = True)
    def __str__(self):
        return self.nome

class Culto(models.Model):
    local = models.ForeignKey(Local, on_delete = models.CASCADE)
    nat_culto = models.ForeignKey(NatCulto, on_delete = models.CASCADE)
    data = models.DateField()
    def __str__(self):
        return f"{self.local} - {self.nat_culto} - {self.data}"