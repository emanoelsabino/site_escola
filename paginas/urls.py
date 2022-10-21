from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('professores/', views.professores, name='professores'),
    path('alunos/', views.alunos, name='alunos'),
    path('alunos/<int:aluno_id>', views.ver_aluno, name='ver_aluno'),
    path('professores/<int:professor_id>', views.ver_professor, name='ver_professor'),
]
