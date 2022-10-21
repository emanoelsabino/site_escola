from django.contrib import admin
from .models import Professor, Aluno, Turma


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nome_pai', 'nome_mae', 'contato_pai', 'contato_mae', 'turma', 'mostrar')
    list_per_page = 25
    list_filter = ('turma',)
    search_fields = ('nome',)
    list_editable = ('mostrar', 'turma')


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'turma')
    list_per_page = 25
    list_filter = ('turma',)
    search_fields = ('nome',)


admin.site.register(Turma)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Aluno, AlunoAdmin)
