from django.contrib import admin
from .models import Aluno
# Register your models here.

class AlunoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
        'data_nascimento',
        'turma'
    ]

admin.site.register(Aluno, AlunoAdmin)