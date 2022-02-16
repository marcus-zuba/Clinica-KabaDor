from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'clinic'

urlpatterns = [
  path('', views.home, name='home'),
  path('galeria/', views.gallery, name='galeria'),
  path('agendamentos', views.list_all_schedules, name='agendamentos'),
  path('meus_agendamentos', views.list_my_schedules, name='meus_agendamentos'),
  path('novo_agendamento/', views.new_schedule, name='novo_agendamento'),
  path('admin_home/', views.admin_home_page, name='admin_home'),
  path('enderecos/', views.list_address, name='enderecos'),
  path('novo_endereco/', views.new_address, name='novo_endereco'),
  path('pacientes/', views.list_patients, name='pacientes'),
  path('funcionarios/', views.list_employees, name='funcionarios'),
  path('buscar_endereco/', views.search_address, name='buscar_endereco'),
  path('listar_especialidades/', views.list_specialty, name='listar_especialidades'),
  path('listar_medicos/', views.list_doctors, name='listar_medicos'),
  path('listar_agenda_medico/', views.list_doctor_schedule, name='listar_agenda_medico')
]
