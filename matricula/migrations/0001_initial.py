# Generated by Django 4.2 on 2023-04-17 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Etapa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etapa_texto', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='Date published')),
            ],
        ),
        migrations.CreateModel(
            name='Requisito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisito_texto', models.CharField(max_length=200)),
                ('etapa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matricula.etapa')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.IntegerField(default=0)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matricula.alumno')),
            ],
        ),
    ]
