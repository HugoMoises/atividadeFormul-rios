from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    endereço = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    email = models.EmailField()
    curso = models.CharField(max_length=100)