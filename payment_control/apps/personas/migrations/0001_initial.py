# Generated by Django 4.1.1 on 2022-10-07 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ajustes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per_names', models.CharField(max_length=30, verbose_name='Nombres')),
                ('per_surnames', models.CharField(max_length=30, verbose_name='Apellidos')),
                ('per_identity_number', models.CharField(max_length=15, verbose_name='Número de Identidad')),
                ('per_birth_date', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('per_personal_phone', models.CharField(max_length=20, verbose_name='Teléfono Personal')),
                ('per_identification_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='per_identification_type', to='ajustes.datosmaestros', verbose_name='Tipo de Identificación')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_address', models.CharField(max_length=40, verbose_name='Dirección')),
                ('nationality_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nationality_type', to='ajustes.datosmaestros', verbose_name='Nacionalidad')),
                ('per_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='personas.person', verbose_name='Persona')),
                ('status_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_type', to='ajustes.datosmaestros', verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Attendant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('att_ocupation', models.CharField(max_length=40, verbose_name='Ocupación')),
                ('att_company', models.CharField(max_length=40, verbose_name='Empresa')),
                ('att_office_phone', models.CharField(max_length=20, verbose_name='Teléfono de Oficina')),
                ('kinship_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kinship_type', to='ajustes.datosmaestros', verbose_name='Tipo de Parentesco')),
                ('per_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='personas.person', verbose_name='Persona')),
            ],
        ),
    ]
