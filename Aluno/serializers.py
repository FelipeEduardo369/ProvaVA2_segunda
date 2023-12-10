from rest_framework import serializers
from .models import Aluno

class AlunoSerializer(serializers.ModelSerializer):
    
    class meta:
        model = Aluno
        
        fields =[
            'nome',
            'sexo',
        ]