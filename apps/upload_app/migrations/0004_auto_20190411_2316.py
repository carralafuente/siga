# Generated by Django 2.2 on 2019-04-12 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_app', '0003_auto_20190411_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='fecha',
            field=models.CharField(max_length=15),
        ),
    ]