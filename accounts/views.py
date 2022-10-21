from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormAluno, FormProfessor


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        print('usuario ou senha incorreto')
        messages.add_message(request, messages.INFO, 'USUÁRIO OU SENHA INCONRRETO!!')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        return redirect('index')


def logout(request):
    auth.logout(request)
    return redirect('index')


def cadastro(request):
    # valida se tem formulario
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    # recebe os dados do formuario
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    # valida se algum campo está vazio
    if not nome or not email or not usuario or not senha or not senha2:
        messages.add_message(request, messages.INFO, 'PREECHA TODOS OS CAMPOS!!!')
        return render(request, 'accounts/cadastro.html')

    # valida email
    try:
        validate_email(email)
    except:
        messages.add_message(request, messages.INFO, 'EMAIL INVÁLIDO!')
        return render(request, 'accounts/cadastro.html')

    # valida senha
    if len(senha) < 6:
        messages.add_message(request, messages.INFO, 'SENHA PRECISA TER NO MÍNIMO 6 CARACTERES!!')
        return render(request, 'accounts/cadastro.html')
    if senha != senha2:
        messages.add_message(request, messages.INFO, 'SENHA NÃO CONFERE!')
        return render(request, 'accounts/cadastro.html')

    # valida se usuario já existe
    if User.objects.filter(username=usuario).exists():
        messages.add_message(request, messages.INFO, 'NOME DE USUÁRIO JÁ EXISTE!')
        return render(request, 'accounts/cadastro.html')

    # valida se emai já existe
    if User.objects.filter(email=email).exists():
        messages.add_message(request, messages.INFO, 'EMAIL JÁ EXISTE!')
        return render(request, 'accounts/cadastro.html')

    messages.add_message(request, messages.INFO, 'CADASTRO REALIZADO COM SUCESSO!')
    user = User.objects.create_user(username=usuario, email=email,
                                    password=senha, first_name=nome, last_name=sobrenome)
    user.save()
    return redirect('index')


@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


@login_required(redirect_field_name='login')
def cad_aluno(request):
    if request.method != 'POST':
        form = FormAluno()
        return render(request, 'accounts/cad_aluno.html', {'form': form})

    form = FormAluno(request.POST)
    if not form.is_valid():
        messages.add_message(request, messages.INFO, 'ERRO, VERIFIQUE AS INFORMAÇÕES PREENCHIDAS!')
        form = FormAluno(request.POST)
        return render(request, 'accounts/cad_aluno.html', {'form': form})

    form.save()
    messages.add_message(request, messages.INFO, 'ALUNO CADASTRADO COM SUCESSO!')
    return redirect('index')


@login_required(redirect_field_name='login')
def cad_professor(request):
    if request.method != 'POST':
        form = FormProfessor()
        return render(request, 'accounts/cad_professor.html', {'form': form})

    form = FormProfessor(request.POST)
    if not form.is_valid():
        messages.add_message(request, messages.INFO, 'ERRO, VERIFIQUE AS INFORMAÇÕES PREENCHIDAS!')
        form = FormProfessor(request.POST)
        return render(request, 'accounts/cad_professor.html', {'form': form})

    form.save()
    messages.add_message(request, messages.INFO, 'PROFESSOR CADASTRADO COM SUCESSO!')
    return redirect('index')
