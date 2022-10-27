from django.shortcuts import render
from rest_framework import viewsets
from apps.personas.models import Person, Student, Attendant, Student_Attendant
from apps.personas.serializer.serializerPerson import PersonSerializer
from apps.personas.serializer.serializerAttendant import AttendantSerializer
from apps.personas.serializer.serializerStudent import StudentSerializer
from apps.personas.serializer.serializerStudent_Attendant import Student_AttendantSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class= PersonSerializer

class AttendantViewSet(viewsets.ModelViewSet):
    queryset = Attendant.objects.all()
    serializer_class= AttendantSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class= StudentSerializer

class Student_AttendantViewSet(viewsets.ModelViewSet):
    queryset = Student_Attendant.objects.all()
    serializer_class= Student_AttendantSerializer

    