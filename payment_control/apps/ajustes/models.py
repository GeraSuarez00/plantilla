from django.db import models

class DatosMaestros(models.Model):
    maes_names=models.CharField(max_length=30, verbose_name="Nombres")
    maes_value=models.CharField(max_length=30, verbose_name="Valor", blank=True)
    maes_dependency=models.CharField(max_length=30, verbose_name="Dependencia",blank=True)
    maes_status_type=models.CharField(max_length=30, verbose_name="Tipo de estado", blank=True)
    
    def __str__(self):
        return (self.maes_names)
        
