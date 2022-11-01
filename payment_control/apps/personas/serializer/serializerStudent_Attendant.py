from apps.personas.models import Student_Attendant
from rest_framework import serializers

class Student_AttendantSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student_Attendant
        fields=['id','sa_stu_id','sa_att_id']

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'sa_stu_id': {
            #    "id":instance.sa_stu_id.per_id.id,
               "id":instance.sa_stu_id.id,
               "nombre": instance.sa_stu_id.per_id.per_names,
               "apellidos": instance.sa_stu_id.per_id.per_surnames,
               "identificación": instance.sa_stu_id.per_id.per_identity_number,
               },
            'sa_att_id': {
               "id":instance.sa_att_id.id,
            #    "id":instance.sa_att_id.per_id.id,
               "nombre": instance.sa_att_id.per_id.per_names,
               "apellidos": instance.sa_att_id.per_id.per_surnames,
               "identificación": instance.sa_att_id.per_id.per_identity_number,
            }
        }