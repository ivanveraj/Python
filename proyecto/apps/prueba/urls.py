from django.urls import path, include
from rest_framework import routers

from apps.prueba.views import PersonaViewSet, AnimalViewSet

router=routers.DefaultRouter()
router.register(r'Persona',PersonaViewSet)
router.register(r'Animal',AnimalViewSet)

urlpatterns=[
    path('',include(router.urls))
]