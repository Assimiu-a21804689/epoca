from django.forms import ModelForm

from epoca.models import Contacto


class ContactoForms(ModelForm):
    class Meta:
        model = Contacto
        fields = "__all__"