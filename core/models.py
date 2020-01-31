from django.db import models


class Cargo(models.Model):
    nome = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name_plural = 'Cargos'
        db_table = 'cargo'


class Pessoa(models.Model):
    nome = models.CharField(max_length=255, null=False)
    admissao = models.DateField()
    cargo = models.ForeignKey('Cargo', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name_plural = 'Pessoas'
        db_table = 'pessoa'
