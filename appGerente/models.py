from django.db import models

# Create your models here.
class Finca(models.Model):
    nombreFinca = models.CharField(max_length=100, null=False)
    nombreGerente = models.CharField(max_length=100, null=False)
    nitFinca = models.IntegerField(unique=True)
    correoGerente = models.CharField(max_length=100, null=False)
    cedulaGerente = models.IntegerField( null=False)
    ubicaciónFinca = models.CharField(max_length=200)

    def __str__(self):
        return self.nombreFinca
