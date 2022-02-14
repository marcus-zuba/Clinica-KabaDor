from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator
from conta.models import Medico

# Create your models here.

class Agenda(models.Model):
  data = models.DateField()
  horario = models.TimeField()
  nome = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  telefone = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{1,14}$')])
  medico = models.ForeignKey(Medico, on_delete=models.CASCADE)