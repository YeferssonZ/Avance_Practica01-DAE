from django.shortcuts import render
from .models import Etapa,Requisito,Alumno,Matricula

#Create your views here.
def index(request):
    lista_etapas = Etapa.objects.all()
    context= {
        'etapas':lista_etapas
    }
    return render(request, 'index.html', context)

# def resolver(request):
#     etapas = Etapa.objects.all()
#     matricula = 0
#     for etapa in etapas:
#         matricula += int (request.POST['etapa_'+str(etapa.id)])

#     context = {
#         'matricula':matricula
#     }

#     return render(request, 'resultados.html', context)


# def registro(request):
#     data_nombre = request.POST['nombre']
#     data_email = request.POST['email']

#     objAlumno = Alumno.objects.create(
#         nombre=data_nombre,
#         email=data_email
#     )

#     context = {
#         'alumnos': [{'nombre': objAlumno.nombre, 'email': objAlumno.email}]
#     }

#     return render(request, 'index.html', context)
