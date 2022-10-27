from inspect import classify_class_attrs
from django.db import models
from apps.ajustes.models import DatosMaestros
class Person(models.Model):
    per_names= models.CharField(max_length=30, verbose_name="Nombres")
    per_surnames= models.CharField(max_length=30, verbose_name="Apellidos")
    per_identity_number= models.CharField(max_length=15, verbose_name="Número de Identidad")
    per_birth_date= models.DateField(verbose_name="Fecha de Nacimiento")
    per_personal_phone=models.CharField(max_length=20,verbose_name="Teléfono Personal")
    per_identification_type=models.ForeignKey(DatosMaestros, verbose_name="Tipo de Identificación", null=True, on_delete=models.CASCADE, related_name='per_identification_type')

    def __str__(self):
        return '%s %s %s' %(self.per_identity_number,self.per_names, self.per_surnames)
class Student(models.Model):
    stu_address=models.CharField(max_length=40, verbose_name="Dirección")
    status_type=models.ForeignKey(DatosMaestros, verbose_name="Estado", null=True, on_delete=models.CASCADE, related_name='status_type')
    nationality_type=models.ForeignKey(DatosMaestros, verbose_name="Nacionalidad", null=True, on_delete=models.CASCADE, related_name='nationality_type')
    per_id=models.ForeignKey(Person, verbose_name="Persona", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' %(self.per_id)

class Attendant(models.Model):
    att_ocupation= models.CharField(max_length=40, verbose_name="Ocupación")
    att_company= models.CharField(max_length=40, verbose_name="Empresa")
    att_office_phone=models.CharField(max_length=20,verbose_name="Teléfono de Oficina")
    kinship_type= models.ForeignKey(DatosMaestros, verbose_name="Tipo de Parentesco", null=True, on_delete=models.CASCADE, related_name='kinship_type')
    per_id=models.ForeignKey(Person, verbose_name="Persona", null=True,on_delete=models.CASCADE)
    stu_id=models.ManyToManyField(Student, through='Student_Attendant', verbose_name="Estudiante")
    
    def __str__(self):
        return '%s' %(self.per_id)
class Student_Attendant(models.Model):
    sa_stu_id=models.ForeignKey(Student, verbose_name="Estudiante", null=True, on_delete=models.CASCADE)
    sa_att_id=models.ForeignKey(Attendant, verbose_name="Acudiente", null=True, on_delete=models.CASCADE)

