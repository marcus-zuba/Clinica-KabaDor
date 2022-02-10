from django.contrib import admin
from .models import BaseDeEnderecos, Pessoa, Paciente, Funcionario, Medico

# Register your models here.

@admin.register(BaseDeEnderecos)
class BaseDeEnderecosAdmin(admin.ModelAdmin):
  pass

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
  pass

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
  pass

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
  pass

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
  pass