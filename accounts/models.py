from django.db import models
from paginas.models import Aluno, Professor
from django import forms


class FormAluno(forms.ModelForm):
    class Meta:
        model = Aluno
        exclude = ()


class FormProfessor(forms.ModelForm):
    class Meta:
        model = Professor
        exclude = ()
