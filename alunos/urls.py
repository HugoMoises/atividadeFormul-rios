from django.urls import path
from .views import alunos, cadastrar_aluno

urlpatterns = [
    path('', alunos, name='alunos'),
    path('cadastrar', cadastrar_aluno, name='cadastrar_aluno'),

]