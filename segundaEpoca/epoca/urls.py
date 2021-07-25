from .views import base, contacto, conetar, disconetar
from django.urls import path
app_name="epoca"
urlpatterns = [
    path('', base, name="base"),
    path('contacto', contacto, name="contacto"),
    path("conectar", conetar, name="conectar"),
    path("disconetar", disconetar, name="disconectar")
]