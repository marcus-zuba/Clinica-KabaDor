from django import forms
from conta.models import Medico
from models import Agenda

class NovoAgendamento(forms.ModelForm):
  especialidade = forms.ModelChoiceField(queryset=Medico.objects.all().values('especialidade'), initial=0)
  class Meta:
    model = Agenda
    fields = ('especialidade', 'data', 'horario', 'nome', 'email', 'telefone')