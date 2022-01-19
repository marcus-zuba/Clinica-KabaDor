from django.core import validators
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator, MaxValueValidator
from cpf_field.models import CPFField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Endereco(models.Model):
  usuario = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='endereco')
  cep = models.IntegerField(validators=[MaxValueValidator(99999999)])
  rua = models.CharField(max_length=50)
  bairro = models.CharField(max_length=50)
  numero = models.IntegerField()
  complemento = models.CharField(max_length=10, null=True)
  def __str__(self):
    return 'Endereço de CEP {} do usuário {}'.format(self.cep, self.usuario.username)


class Conta(models.Model):
  usuario = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='conta')
  nome_completo = models.CharField(max_length=100)
  cpf = CPFField('cpf')
  telefone = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{1,14}$')])
  def __str__(self):
    return 'Conta do usuário {}'.format(self.usuario.username)

@receiver(post_save, sender=User)
def update_user(sender, instance, created, **kwargs):
  if created:
    Conta.objects.create(usuario=instance, nome_completo="123", cpf="123", telefone="123")
    Endereco.objects.create(usuario=instance, cep="123", rua="123", bairro="123", numero=123, complemento="")
    instance.conta.save()
    instance.endereco.save()

