from django.db import models

# Create your models here.
class DetalheDisciplina(models.Model):
    codigocurso = models.CharField(max_length=100) 
    codigodisciplina = models.CharField(max_length=100)