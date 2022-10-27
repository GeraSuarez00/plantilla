from apps.personas.models import Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student    
        fields=['id','stu_address','status_type','nationality_type','per_id']

    def to_representation(self, instance):
        return {
           'id':instance.id,
           'stu_address': instance.stu_address,
           'status_type': {
            'nombre': instance.status_type.maes_names,
            'id': instance.status_type.id
            },
           'nationality_type': {
            'nombre': instance.nationality_type.maes_names,
            'id': instance.nationality_type.id
            },
           'per_id': {
            'nombre': instance.per_id.per_names,
            'apellidos':instance.per_id.per_surnames,
            'identificación': instance.per_id.per_identity_number,   
            'id': instance.per_id.id
            }
        }
