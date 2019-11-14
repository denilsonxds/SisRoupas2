from django.db import models
from cadastro.models import *
# Create your models here.

class Taxas(models.Model):

    tipo_taxa = models.CharField(max_length=30, blank=True, null=True)
    valor_taxa = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.tipo_taxa
        
class Aluguel(models.Model):

    roupa = models.ForeignKey(Roupa, on_delete='CASCADE')
    valor = models.ForeignKey(Valor, on_delete='CASCADE')
    data_retirada = models.DateField()
    data_devolucao = models.DateField(blank=True, null=True)
    taxa = models.ForeignKey(Taxas, on_delete="CASCADE")

    def __str__(self):
        return "Roupa " + self.roupa + " Alugada"