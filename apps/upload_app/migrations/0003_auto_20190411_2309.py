# Generated by Django 2.2 on 2019-04-12 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_app', '0002_auto_20190411_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='upload',
            name='folio',
            field=models.IntegerField(),
        ),
    ]