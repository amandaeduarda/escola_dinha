from django.db import models

# Create your models here.
class Turma(models.Model):
    nome = models.CharField(max_length=20)
    ano_letivo = models.IntegerField(
        choices=(
            (2020, 2020),
            (2021, 2021),
            (2022, 2022),            
        )
    )

    def __str__(self):
        return self.nome + '/' + str(self.ano_letivo)
    
