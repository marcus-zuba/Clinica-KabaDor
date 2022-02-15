from django import forms
from conta.models import Medico
from .models import Agenda

class NovoAgendamento(forms.ModelForm):
  class Meta:
    model = Agenda
    fields = ('data', 'horario', 'nome', 'email', 'telefone')