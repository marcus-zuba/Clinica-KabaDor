from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from conta.models import BaseDeEnderecos, Pessoa, Paciente, Funcionario, Medico
from clinic.dados_clinicos import TIPOS_SANGUINEOS, ESPECIALIDADES_MEDICAS
import datetime

class LoginForm(AuthenticationForm):

  def __init__(self, * args, ** kwargs):
    super(LoginForm, self).__init__( * args, ** kwargs)

  usuario = forms.CharField()
  senha = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
  username = forms.CharField(label='Usuario')
  email = forms.EmailField(label='Email')
  password = forms.CharField(label='Senha',widget=forms.PasswordInput)
  password2 = forms.CharField(label='Repita a senha',widget=forms.PasswordInput)
  class Meta:
    model = User
    fields = ('username', 'email',)
  def clean_password2(self):
    cd = self.cleaned_data
    if cd['password'] != cd['password2']:
      raise forms.ValidationError('Passwords don\'t match.')
    return cd['password2']

class UserUpdateForm(forms.ModelForm):
  username = forms.CharField(label='Usuario')
  email = forms.EmailField(label='Email')
  class Meta:
    model = User
    fields = ('username', 'email',)

class PessoaRegistrationForm(forms.ModelForm):
  class Meta:
    model = Pessoa
    fields = ('nome', 'telefone', 'cep', 'logradouro', 'bairro', 'cidade', 'estado')

class PessoaCompletaRegistrationForm(forms.ModelForm):
  class Meta:
    model = Pessoa
    fields = ('nome', 'email', 'telefone', 'cep', 'logradouro', 'bairro', 'cidade', 'estado')

class PacienteRegistrationForm(forms.ModelForm):
  tipo_sanguineo = forms.ChoiceField(choices=TIPOS_SANGUINEOS)
  class Meta:
    model = Paciente
    fields = ('peso', 'altura', 'tipo_sanguineo')

class FuncionarioRegistrationForm(forms.ModelForm):
  data_contrato = forms.DateField(widget=forms.SelectDateWidget(years=[2015,2016,2017,2018,2019,2020,2021,2022]), initial=datetime.date.today)
  class Meta:
    model = Funcionario
    fields = ('data_contrato', 'salario')
  def clean(self):
    data = self.cleaned_data["data_contrato"]
    if data > datetime.date.today():
      raise forms.ValidationError("A data não pode ser no futuro!")

class MedicoRegistrationForm(forms.ModelForm):
  especialidade = forms.ChoiceField(choices=ESPECIALIDADES_MEDICAS)
  class Meta:
    model = Medico
    fields = ('especialidade', 'crm')

class EnderecoRegistrationForm(forms.ModelForm):
  class Meta:
    model = BaseDeEnderecos
    fields = ('cep', 'logradouro', 'bairro', 'cidade', 'estado')