# Generated by Django 2.2 on 2019-04-05 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trabajador_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_cliente', models.IntegerField()),
                ('razonsocial', models.CharField(max_length=70)),
                ('rfc', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=254)),
                ('fecha_alta', models.DateField()),
                ('estado', models.CharField(max_length=15)),
                ('vendedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trabajador_app.Trabajador')),
            ],
        ),
    ]
