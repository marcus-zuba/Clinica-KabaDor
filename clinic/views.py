from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from conta.forms import EnderecoRegistrationForm
from conta.models import BaseDeEnderecos, Pessoa, Funcionario

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

def list_address(request):
  addresses = BaseDeEnderecos.objects.all()
  return render(request, "clinic/address.html", {'addresses': addresses})

def list_patients(request):
  persons = Pessoa.objects.exclude(paciente__isnull=True)
  return render(request, "clinic/patient.html", {'persons': persons})

def list_employees(request):
  employees = Funcionario.objects.exclude(medico__isnull=False)
  doctors = Funcionario.objects.exclude(medico__isnull=True)
  return render(request, "clinic/employee.html", {'employees':employees,'doctors':doctors})

def new_schedule(request):
  return render(request, "clinic/new_schedule.html", {})

@login_required
def admin_home_page(request):
  return render(request, "clinic/admin_home_page.html")