from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='index_login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cad_aluno/', views.cad_aluno, name='cad_aluno'),
    path('cad_professor/', views.cad_professor, name='cad_professor'),
]
