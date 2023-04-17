from django.contrib import admin

# Register your models here.
from .models import Etapa, Requisito, Alumno, Matricula

admin.site.register(Etapa)
admin.site.register(Requisito)