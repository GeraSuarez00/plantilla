from django.shortcuts import render
from rest_framework import viewsets
from apps.matricula.models import Registration, Payment
from apps.matricula.serializer.serializerRegistration import RegistrationSerializer
from apps.matricula.serializer.serializerPayment import PaymentSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class= RegistrationSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class= PaymentSerializer

    