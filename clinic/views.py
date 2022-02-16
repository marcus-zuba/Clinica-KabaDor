from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NovoAgendamento
from conta.forms import EnderecoRegistrationForm
from.models import Agenda
from conta.models import BaseDeEnderecos, Pessoa, Funcionario, Medico

# Create your views here.

def home(request):
  return render(request, "clinic/home.html", {})

def gallery(request):
  return render(request, "clinic/gallery.html", {})

def new_address(request):
  if request.method == 'POST':
    endereco_form = EnderecoRegistrationForm(request.POST)
    if endereco_form.is_valid():
      endereco_form.save()
      return render(request, "clinic/new_address_complete.html", {})
  else:
    endereco_form = EnderecoRegistrationForm()
  return render(request, "clinic/new_address.html", {'endereco_form': endereco_form})

@login_required
def list_address(request):
  addresses = BaseDeEnderecos.objects.all()
  return render(request, "clinic/address.html", {'addresses': addresses})

@login_required
def list_patients(request):
  persons = Pessoa.objects.exclude(paciente__isnull=True)
  return render(request, "clinic/patient.html", {'persons': persons})

@login_required
def list_employees(request):
  employees = Funcionario.objects.exclude(medico__isnull=False)
  doctors = Funcionario.objects.exclude(medico__isnull=True)
  return render(request, "clinic/employee.html", {'employees':employees,'doctors':doctors})

def new_schedule(request):
  if request.method == 'POST':
    form = NovoAgendamento(request.POST)
    if form.is_valid():
      form.save()
      return render(request, "clinic/new_schedule_complete.html", {})
  else:
    form = NovoAgendamento()
  return render(request, "clinic/new_schedule.html", {'form':form})

@login_required
def list_all_schedules(request):
  agendamentos = Agenda.objects.all()
  return render(request, "clinic/schedules.html", {'agendamentos':agendamentos, 'todos':True})

@login_required
def list_my_schedules(request):
  medico = request.user.pessoa.funcionario.medico
  if not medico:
    return redirect('/clinica/admin_home/')
  else:
    agendamentos = Agenda.objects.filter(medico=medico)
    return render(request, "clinic/schedules.html", {'agendamentos':agendamentos, 'todos':False})

@login_required
def admin_home_page(request):
  return render(request, "clinic/admin_home_page.html")

def search_address(request):
  cep = request.GET.get('cep')
  endereco = BaseDeEnderecos.objects.filter(cep=cep)
  if not endereco:
    return HttpResponse("CEP não encontrado", status=404)
  else:
    return JsonResponse(list(endereco.values('cep','logradouro','bairro','cidade','estado')),safe=False)

def list_specialty(request):
  especialidades = Medico.objects.all().values('especialidade')
  lista_especialidades = []
  for especialidade in especialidades:
    lista_especialidades.append(especialidade['especialidade'])
  lista_especialidades=list(dict.fromkeys(lista_especialidades))
  if not lista_especialidades:
    return HttpResponse("Não há médicos cadastrados", status=404)
  else:
    return JsonResponse(lista_especialidades, safe=False)

def list_doctors(request):
  especialidade = request.GET.get('especialidade')
  medicos = Medico.objects.filter(especialidade=especialidade).values('id', 'funcionario')
  for medico in medicos:
    medico["nome"]=(Funcionario.objects.get(pk=medico['funcionario']).pessoa.nome)
  if not medicos:
    return HttpResponse("Não há médicos cadastrados com a especialidade solicitada", status=404)
  else:
    return JsonResponse(list(medicos), safe=False)

def list_doctor_schedule(request):
  id_doctor = request.GET.get('id_doctor')
  data = request.GET.get('data')
  horarios_ocupados = Agenda.objects.filter(medico=id_doctor, data=data).values('horario')
  horarios = ["08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00"]
  for horario in list(horarios_ocupados):
    horarios.remove(horario['horario'].strftime("%H:00"))
  if not horarios:
    return HttpResponse("Não há horários disponíveis", status=404)
  else:
    return JsonResponse(horarios, safe=False)