from django.shortcuts import render
from rest_framework import viewsets
from apps.ajustes.models import DatosMaestros
from apps.ajustes.serializer import DatosMaestrosSerializer

class DatosMaestrosViewSet(viewsets.ModelViewSet):
    queryset = DatosMaestros.objects.all()
    serializer_class= DatosMaestrosSerializer