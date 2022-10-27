from django.db import models
from multiselectfield import MultiSelectField
from apps.personas.models import Student
from apps.ajustes.models import DatosMaestros

class Registration(models.Model):
    reg_year= models.DateField(verbose_name="Año")
    reg_value= models.FloatField(verbose_name="Valor")
    reg_course_type= models.ForeignKey(DatosMaestros,verbose_name="Curso", null=True, on_delete=models.CASCADE,  related_name='reg_course_type')
    reg_group_type= models.ForeignKey(DatosMaestros,verbose_name="Grupo", null=True, on_delete=models.CASCADE,  related_name='reg_group_type')
    student_history_type= models.ForeignKey(DatosMaestros,verbose_name="Histórico de estudiante", null=True, on_delete=models.CASCADE,  related_name='student_history_type')
    school_level= models.ForeignKey(DatosMaestros,verbose_name="Nivel escolar", null=True, on_delete=models.CASCADE, related_name='school_level')
    regist_status_type= models.ForeignKey(DatosMaestros,verbose_name="Estado de matrícula", null=True, on_delete=models.CASCADE, related_name='regist_status_type')
    stu_id= models.ForeignKey(Student,verbose_name="Estudiante", null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return '%s' %(self.stu_id)
        
month_choices = (
('Febrero','Febrero'),
('Marzo','Marzo'),
('Abril','Abril'),
('Mayo','Mayo'),
('Junio','Junio'),
('Julio','Julio'),
('Agosto','Agosto'),
('Septiembre','Septiembre'),
('Octubre','Octubre'),
('Noviembre','Noviembre'),
)

    
class Payment(models.Model):
 
    pay_date= models.DateField(verbose_name="Fecha de pago")
    pay_value= models.FloatField(verbose_name="Valor")
    pay_discount= models.FloatField(verbose_name="Descuento")
    pay_month= MultiSelectField(max_length=200,verbose_name="Mes a pagar", choices=month_choices)
    pay_total_value= models.FloatField(verbose_name="Valor Total")
    payment_type= models.ForeignKey(DatosMaestros,verbose_name="Tipo de Pago", null=True, on_delete=models.CASCADE, related_name='payment_type')
    item_type= models.ForeignKey(DatosMaestros,verbose_name="Concepto", null=True, on_delete=models.CASCADE, related_name='item_type')
    payment_method_type= models.ForeignKey(DatosMaestros,verbose_name="Método de Pago", null=True, on_delete=models.CASCADE, related_name='payment_method_type')
    reg_id=models.ForeignKey(Registration, verbose_name="Matrícula", null=True, on_delete=models.CASCADE)

