from django.db import models

# Create your models here.
class DetalheTurma(models.Model):
    CodigoAluno = models.CharField(max_length=100) 
    CodigoProfessor = models.CharField(max_length=100)
    CodigoTurma = models.CharField(max_length=100)