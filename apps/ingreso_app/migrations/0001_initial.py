# Generated by Django 2.2 on 2019-04-03 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_factura', models.DateField()),
                ('importe', models.DecimalField(decimal_places=2, max_digits=2)),
                ('factura', models.CharField(max_length=10)),
                ('tipo_producto', models.CharField(max_length=45)),
            ],
        ),
    ]