from django import forms
from conta.models import Medico
from .models import Agenda
import datetime

class NovoAgendamento(forms.ModelForm):
  medico = forms.ModelChoiceField(queryset=Medico.objects.all())
  data = forms.DateField(widget=forms.SelectDateWidget(), initial=datetime.date.today)
  horario = forms.CharField(widget=forms.Select)
  class Meta:
    model = Agenda
    fields = ('medico', 'data', 'horario', 'nome', 'email', 'telefone')
  def clean(self):
    # print(self.data)
    # print(self.cleaned_data)
    data = self.cleaned_data["data"]
    horario = self.cleaned_data["horario"]
    if data < datetime.date.today():
      raise forms.ValidationError("A data não pode ser no passado!")
    elif data == datetime.date.today():
      if datetime.datetime.strptime(horario,'%H:%M').time() < datetime.datetime.now().time():
        raise forms.ValidationError("Na data de hoje, o horário não pode ser anterior ao horário atual!")