# Generated by Django 2.2 on 2019-04-11 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('serie', models.CharField(max_length=1)),
                ('folio', models.CharField(max_length=15)),
                ('cliente', models.CharField(max_length=15)),
                ('razonsocial', models.CharField(max_length=75)),
                ('rfc', models.CharField(max_length=15)),
                ('estado', models.CharField(max_length=15)),
                ('neto', models.CharField(max_length=15)),
                ('descuentos', models.CharField(max_length=15)),
                ('impuestos', models.CharField(max_length=15)),
                ('total', models.CharField(max_length=15)),
            ],
        ),
    ]
