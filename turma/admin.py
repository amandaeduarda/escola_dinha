from django.contrib import admin
from .models import Turma

# Register your models here.
class TurmaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
        'ano_letivo'
    ]

admin.site.register(Turma, TurmaAdmin)