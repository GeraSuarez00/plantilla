from apps.personas.models import Attendant
from rest_framework import serializers

class AttendantSerializer(serializers.ModelSerializer):
    class Meta:
        model= Attendant
        fields= ['id','att_ocupation','att_company','att_office_phone','kinship_type','per_id']
    def to_representation(self, instance):
        return {
            'id':instance.id,
            'att_ocupation':instance.att_ocupation,
            'att_company':instance.att_company,
            'att_office_phone':instance.att_office_phone,
            'kinship_type':{
               'nombre': instance.kinship_type.maes_names,
               'id': instance.kinship_type.id

            },
            'per_id': {
                'nombre': instance.per_id.per_names,
                'apellidos':instance.per_id.per_surnames,
                'identificación': instance.per_id.per_identity_number,   
                'id': instance.per_id.id
            }
        }