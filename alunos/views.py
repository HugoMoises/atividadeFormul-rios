from django.shortcuts import render, redirect
from .models import Aluno
from .forms import AlunoForm
# Create your views here.

def alunos(request):
    alunos = Aluno.objects.all()
    contexto = {
        'alunos': alunos
    }
    return render(request, 'alunos/alunos.html', contexto)

def cadastrar_aluno(request):
    form = AlunoForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('alunos')
    else: 
        form = AlunoForm()
    contexto = {
        'form': form
    }
    return render(request, 'alunos/cadastrar_aluno.html', contexto)