from django.db import models

# Create your models here.

class JSONCLP(models.Model):
    Sensor = models.BooleanField(blank=False, null=False)
    Botao = models.BooleanField(blank=False, null=False)
    LigaRobo = models.BooleanField(blank=False, null=False)
    ResetContador = models.BooleanField(blank=False, null=False)
    Valor_Contagem = models.IntegerField(blank=False, null=False)

    def __str__(self) -> str:
        return "JSON CLP"
    
     