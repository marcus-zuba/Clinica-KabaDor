from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . import forms

app_name = 'conta'

urlpatterns = [
  path('cadastrar_funcionario/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
  path('cadastrar_paciente/', views.cadastrar_paciente, name='cadastrar_paciente'),
  path('login/', auth_views.LoginView.as_view(),name='login'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('trocar_senha/',auth_views.PasswordChangeView.as_view(success_url="sucesso/"),name='password_change'),
  path('trocar_senha/sucesso/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
  path('redefinir_senha/',auth_views.PasswordResetView.as_view(),name='redefinir_senha'),
  path('redefinir_senha/sucesso/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
  path('redefinir/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='redefinir_senha_confirmacao'),
  path('redefinir/concluido/',auth_views.PasswordResetCompleteView.as_view(),name='redefinir_senha_concluido'),
  path('atualizar/', views.atualizar_pessoa, name='atualizar_pessoa')
]
