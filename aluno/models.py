from django.db import models
from turma.models import Turma

# Create your models here.
class Aluno(models.Model):
    data_matricula = models.DateField(auto_now=True)
    nome = models.CharField(
        max_length=50
    )
    data_nascimento = models.DateField()
    turma = models.ForeignKey(
        Turma,
        null=True,
        on_delete=models.PROTECT
    )
    observacao = models.TextField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nome
