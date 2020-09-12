from django.shortcuts import render
from .models import Aluno

# Create your views here.
def alunos(request):
    data = {
        'title' : 'Escola da Dinha',
        'alunos' : Aluno.objects.all()
    }

    return render(request, 'aluno/dados_aluno.html', data)