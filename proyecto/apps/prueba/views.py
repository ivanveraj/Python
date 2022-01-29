from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from apps.prueba.models import Persona, Animal
from apps.prueba.serializer import PersonaSerializer, AnimalSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    @action(detail=True)
    def Mascotas(self, request, pk, *kwargs):
        mascotas=Animal.objects.filter(dueno=pk)
        serializer=AnimalSerializer(mascotas,many=True)
        return Response({'mascotas':serializer.data})
class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
