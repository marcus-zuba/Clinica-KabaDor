from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'clinic'

urlpatterns = [
  path('', views.home, name='home'),
  path('galeria/', views.gallery, name='galeria'),
  path('novo_endereco/', views.new_address, name='novo_endereco'),
  path('agendamento', views.new_schedule, name='agendamento'),
  path('admin_home/', views.admin_home_page, name='admin_home'),
  path('enderecos/', views.list_address, name='enderecos'),
  path('pacientes/', views.list_patients, name='pacientes'),
  path('funcionarios/', views.list_employees, name='funcionarios')
]
