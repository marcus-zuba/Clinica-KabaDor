from django.core import validators
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class BaseDeEnderecos(models.Model):
  cep = models.IntegerField(validators=[MaxValueValidator(99999999)], unique=True)
  logradouro = models.CharField(max_length=50)
  bairro = models.CharField(max_length=50)
  cidade = models.CharField(max_length=50)
  estado = models.CharField(max_length=50)
  def __str__(self):
    return 'Endereço de CEP {}'.format(self.cep)

class Pessoa(models.Model):
  usuario = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='pessoa', null=True)
  nome = models.CharField(max_length=100)
  email = models.CharField(max_length=100, unique=True)
  telefone = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{1,14}$')])
  cep = models.IntegerField(validators=[MaxValueValidator(99999999)])
  logradouro = models.CharField(max_length=50)
  bairro = models.CharField(max_length=50)
  cidade = models.CharField(max_length=50)
  estado = models.CharField(max_length=50)
  def __str__(self):
    return 'Pessoa {} de email {}'.format(self.nome, self.email)

class Paciente(models.Model):
  pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE, related_name='paciente')
  peso = models.FloatField()
  altura = models.FloatField()
  tipo_sanguineo = models.CharField(max_length=3)
  def __str__(self):
    return 'Paciente {} de email {}'.format(self.pessoa.nome, self.pessoa.email)

class Funcionario(models.Model):
  pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE, related_name='funcionario')
  data_contrato = models.DateField()
  salario = models.FloatField()
  def __str__(self):
    return 'Funcionário {} de email {}'.format(self.pessoa.nome, self.pessoa.email)

class Medico(models.Model):
  funcionario = models.OneToOneField(Funcionario, on_delete=models.CASCADE, related_name='medico')
  especialidade = models.CharField(max_length=50)
  crm = models.IntegerField()
  def __str__(self):
    return 'Médico {} de email {}'.format(self.funcionario.pessoa.nome, self.funcionario.pessoa.email)
