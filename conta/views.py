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
def painel_usuario(request):
  return render(request, 'conta/painel_usuario.html', {})

@login_required
def atualizar_conta(request):
  pass
  # if request.method == 'POST':
  #   form_pessoa = PessoaRegistrationForm(request.POST, instance=request.user.pessoa)
  #   form_funcionario = FuncionarioRegistrationForm(request.POST, instance=request.user.pessoa.funcionario)
  #   if form_pessoa.is_valid() and form_funcionario.is_valid():
  #     form_pessoa.save()
  #     form_funcionario.save()
  #     messages.success(request, 'Informações atualizadas com sucesso!')
  #   else:
  #     messages.error(request, 'Erro na atualização das informações!')
  #   return redirect('/conta/')
  # else:
  #   form_pessoa = PessoaRegistrationForm(instance=request.user.pessoa)
  #   form_funcionario = FuncionarioRegistrationForm(instance=request.user.pessoa.funcionario)
  #   if(request.user.pessoa.funcionario.medico):
  #     form_medico = MedicoRegistrationForm(instance=request.user.pessoa.funcionario.medico)
  #   else:
  #     form_medico = None
  # return render(request, 'conta/atualizar_conta.html', {'form_pessoa': form_pessoa, 'form_funcionario':form_funcionario, 'form_medico':form_medico})

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
      if user_form.is_valid() and pessoa_form.is_valid() and funcionario_form.is_valid():
        novo_user = user_form.save(commit=False)
        novo_user.set_password(user_form.cleaned_data['password'])
        novo_user.save()
        novo_user.refresh_from_db()
        nova_pessoa = pessoa_form.save(commit=False)
        nova_pessoa.usuario = novo_user
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

  # if request.method == 'POST':
  #   user_form = UserRegistrationForm(request.POST)
  #   conta_form = ContaRegistrationForm(request.POST)
  #   endereco_form = EnderecoCompletoRegistrationForm(request.POST)
  #   if user_form.is_valid() and conta_form.is_valid() and endereco_form.is_valid():
  #     new_user = user_form.save(commit=False)
  #     new_user.set_password(user_form.cleaned_data['password'])
  #     # Save the User object
  #     new_user.save()
  #     new_user.refresh_from_db()
  #     conta_form = ContaRegistrationForm(request.POST, instance=new_user.conta)
  #     conta_form.full_clean()
  #     conta_form.save()
  #     endereco_form = EnderecoCompletoRegistrationForm(request.POST, instance=new_user.endereco)
  #     endereco_form.full_clean()
  #     endereco_form.save()
  #     return render(request,'conta/cadastro_completo.html',{'new_user': new_user})
  # else:
  #   user_form = UserRegistrationForm()
  #   conta_form = ContaRegistrationForm()
  #   endereco_form = EnderecoCompletoRegistrationForm()
  # return render(request,'conta/cadastro.html',
  #   {'user_form': user_form, 
  #     'conta_form': conta_form,
  #     'endereco_form': endereco_form})