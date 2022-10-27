from apps.personas.models import Person
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model= Person
        fields=['id','per_names','per_surnames','per_identity_number','per_birth_date','per_personal_phone','per_identification_type']

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'per_names':instance.per_names,
            'per_surnames':instance.per_surnames,
            'per_identity_number':instance.per_identity_number,
            'per_birth_date':instance.per_birth_date,
            'per_personal_phone':instance.per_personal_phone,'per_identification_type':instance.per_identification_type.maes_names
        }
