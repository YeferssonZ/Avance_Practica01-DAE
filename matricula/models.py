from django.db import models

#Create your models here.

class Etapa(models.Model):
    etapa_texto = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')

    def __str__(self):
        return self.etapa_texto
    
class Requisito(models.Model):
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    requisito_texto = models.CharField(max_length=200)
    puntos = models.IntegerField(default=0)

    def __srt__(self):
        return self.requisito_texto

class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Matricula(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    completados = models.IntegerField(default=0)
    pendientes = models.IntegerField(default=0)
    matricula = models.IntegerField(default=0)

    def __str__(self):
        return self.matricula