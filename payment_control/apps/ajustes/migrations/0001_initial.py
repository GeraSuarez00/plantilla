# Generated by Django 4.1.1 on 2022-10-07 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosMaestros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maes_names', models.CharField(max_length=30, verbose_name='Nombres')),
                ('maes_value', models.CharField(blank=True, max_length=30, verbose_name='Valor')),
                ('maes_dependency', models.CharField(blank=True, max_length=30, verbose_name='Dependencia')),
                ('maes_status_type', models.CharField(blank=True, max_length=30, verbose_name='Tipo de estado')),
            ],
        ),
    ]