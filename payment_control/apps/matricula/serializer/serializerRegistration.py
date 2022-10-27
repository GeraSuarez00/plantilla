from apps.matricula.models import Registration
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=Registration
        # fields='__all__'
        fields= ['id','reg_year','reg_value','reg_course_type','reg_group_type','student_history_type','school_level','regist_status_type','stu_id']
        
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'reg_year': instance.reg_year,   
            'reg_value': instance.reg_value,   
            'reg_course_type':{
               'nombre': instance.reg_course_type.maes_names,
               'id': instance.reg_course_type.id
            },
            'reg_group_type':{
                'nombre': instance.reg_group_type.maes_names,
                'id': instance.reg_group_type.id
            },
            'student_history_type':{
                'nombre': instance.student_history_type.maes_names,
                'id': instance.student_history_type.id
            },
            'school_level':{
                'nombre': instance.school_level.maes_names,
                'id': instance.school_level.id
            },
            'regist_status_type':{
                'nombre': instance.regist_status_type.maes_names,
                'id': instance.regist_status_type.id
            },
            'stu_id':{
                'nombre': instance.stu_id.per_id.per_names,
                'apellidos':instance.stu_id.per_id.per_surnames,
                'identificación':  instance.stu_id.per_id.per_identity_number,   
                'id': instance.stu_id.per_id.id
            }
        }