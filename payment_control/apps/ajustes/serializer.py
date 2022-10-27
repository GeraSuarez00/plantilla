from apps.ajustes.models import DatosMaestros
from rest_framework import serializers

class DatosMaestrosSerializer(serializers.ModelSerializer):
    class Meta:
        model=DatosMaestros
        fields='__all__'
