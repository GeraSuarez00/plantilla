# Generated by Django 4.1.1 on 2022-10-09 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ajustes', '0001_initial'),
        ('matricula', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='reg_course',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='reg_group',
        ),
        migrations.AddField(
            model_name='registration',
            name='reg_course_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reg_course_type', to='ajustes.datosmaestros', verbose_name='Curso'),
        ),
        migrations.AddField(
            model_name='registration',
            name='reg_group_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reg_group_type', to='ajustes.datosmaestros', verbose_name='Grupo'),
        ),
    ]
