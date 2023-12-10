from django.db import models

# Create your models here.
class Curso(models.Model):
    Codigo = models.CharField(max_length=100) 
    Nome = models.CharField(max_length=100)