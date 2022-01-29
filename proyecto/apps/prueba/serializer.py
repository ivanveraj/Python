from rest_framework import serializers
from apps.prueba.models import Persona, Animal


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Persona
        fields='__all__'
    def create(self, validated_data):
        return Persona.objects.create(**validated_data)
class AnimalSerializer(serializers.ModelSerializer):
    '''dueno=PersonaSerializer(read_only=True)'''
    persona=serializers.SerializerMethodField()
    def get_persona(self,Animal):
        persona=Persona.objects.get(id=Animal.dueno.id)
        return PersonaSerializer(persona).data
    class Meta:
        model= Animal
        fields='__all__'
