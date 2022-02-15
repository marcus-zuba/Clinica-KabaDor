from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, EnderecoRegistrationForm
from .forms import PessoaRegistrationForm, PessoaCompletaRegistrationForm, PacienteRegistrationForm
from .forms import FuncionarioRegistrationForm, MedicoRegistrationForm
from django.contrib import messages

# Create your views here.

def login_usuario(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      usuario = authenticate(request,
                          username=cd['usuario'],
                          password=cd['senha'])
      if usuario is not None:
        if usuario.is_active:
          login(request, usuario)
  else:
    form = LoginForm()
  return render(request, 'conta/login.html', {'form': form})

@login_required
def atualizar_pessoa(request):
  if request.method == 'POST':
    form_pessoa = PessoaRegistrationForm(request.POST, instance=request.user.pessoa)
    if form_pessoa.is_valid():
      form_pessoa.save()
      return render(request,'conta/atualizacao_completa.html',{})
  else:
    form_pessoa = PessoaRegistrationForm(instance=request.user.pessoa)
  return render(request, 'conta/atualizar_pessoa.html', {'form_pessoa': form_pessoa})

def cadastrar_funcionario(request):
  if request.method == 'POST':
    user_form = UserRegistrationForm(request.POST)
    pessoa_form = PessoaRegistrationForm(request.POST)
    funcionario_form = FuncionarioRegistrationForm(request.POST)
    if(request.POST.get("tipo_funcionario")=="medico"):
      medico_form = MedicoRegistrationForm(request.POST)
      if (user_form.is_valid() and pessoa_form.is_valid() 
      and funcionario_form.is_valid() and medico_form.is_valid()):
        novo_user = user_form.save()
        nova_pessoa = pessoa_form.save(commit=False)
        nova_pessoa.usuario = novo_user
        nova_pessoa.email = novo_user.email
        nova_pessoa.save()
        nova_pessoa.refresh_from_db()
        novo_funcionario = funcionario_form.save(commit=False)
        novo_funcionario.pessoa = nova_pessoa
        novo_funcionario.save()
        novo_funcionario.refresh_from_db()
        novo_medico = medico_form.save(commit=False)
        novo_medico.funcionario = novo_funcionario
        novo_medico.save()
        novo_medico.refresh_from_db()
        return render(request,'conta/cadastro_completo.html',{})
    else:
      medico_form = MedicoRegistrationForm()
      if user_form.is_valid() and pessoa_form.is_valid() and funcionario_form.is_valid():
        novo_user = user_form.save(commit=False)
        novo_user.set_password(user_form.cleaned_data['password'])
        novo_user.save()
        novo_user.refresh_from_db()
        nova_pessoa = pessoa_form.save(commit=False)
        nova_pessoa.usuario = novo_user
        nova_pessoa.email = novo_user.email
        nova_pessoa.save()
        nova_pessoa.refresh_from_db()
        novo_funcionario = funcionario_form.save(commit=False)
        novo_funcionario.pessoa = nova_pessoa
        novo_funcionario.save()
        novo_funcionario.refresh_from_db()
        return render(request,'conta/cadastro_completo.html',{})
  else:
    user_form = UserRegistrationForm()
    pessoa_form = PessoaRegistrationForm()
    funcionario_form = FuncionarioRegistrationForm()
    medico_form = MedicoRegistrationForm()
  return render(request, 'conta/cadastro_funcionario.html',
    {'user_form': user_form,
    'pessoa_form':pessoa_form,
    'funcionario_form':funcionario_form,
    'medico_form':medico_form})

def cadastrar_paciente(request):
  if request.method == 'POST':
    pessoa_form = PessoaCompletaRegistrationForm(request.POST)
    paciente_form = PacienteRegistrationForm(request.POST)
    if pessoa_form.is_valid() and paciente_form.is_valid():
      nova_pessoa = pessoa_form.save(commit=False)
      nova_pessoa.save()
      nova_pessoa.refresh_from_db()
      novo_paciente = paciente_form.save(commit=False)
      novo_paciente.pessoa = nova_pessoa
      novo_paciente.save()
      novo_paciente.refresh_from_db()
      return render(request,'conta/cadastro_completo.html',{})
  else:
    pessoa_form = PessoaCompletaRegistrationForm()
    paciente_form = PacienteRegistrationForm()
  return render(request,'conta/cadastro_paciente.html', 
    {'pessoa_form':pessoa_form, 
    'paciente_form':paciente_form})

