from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Professor, Aluno
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


@login_required(redirect_field_name='login')
def professores(request):
    professores = Professor.objects.order_by('nome')
    paginator = Paginator(professores, 10)

    page = request.GET.get('p')
    professores = paginator.get_page(page)

    return render(request, 'professores.html', {
        'professores': professores
    })


@login_required(redirect_field_name='login')
def alunos(request):
    alunos = Aluno.objects.order_by('nome').filter(
        mostrar=True
    )
    paginator = Paginator(alunos, 10)

    page = request.GET.get('p')
    alunos = paginator.get_page(page)

    return render(request, 'alunos.html', {
        'alunos': alunos
    })


@login_required(redirect_field_name='login')
def ver_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)

    if not aluno.mostrar:
        raise Http404()

    return render(request, 'ver_aluno.html', {
        'aluno': aluno
    })


@login_required(redirect_field_name='login')
def ver_professor(request, professor_id):
    professor = get_object_or_404(Professor, id=professor_id)
    return render(request, 'ver_professor.html', {
        'professor': professor
    })
