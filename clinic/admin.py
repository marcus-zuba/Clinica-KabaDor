from django.contrib import admin
from .models import Agenda

# Register your models here.

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
  pass
