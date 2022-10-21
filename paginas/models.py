from django.db import models


class Turma(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome


class Professor(models.Model):
    nome = models.CharField(max_length=255)
    turma = models.ForeignKey(Turma, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    nome_pai = models.CharField(max_length=255)
    nome_mae = models.CharField(max_length=255)
    contato_pai = models.CharField(max_length=255, blank=True)
    contato_mae = models.CharField(max_length=255)
    turma = models.ForeignKey(Turma, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
