from django.db import models

# Create your models here.
class DetalhesCurso(models.Model):
    CodigoCurso = models.CharField(max_length=100) 
    CodigoTurma = models.CharField(max_length=100)