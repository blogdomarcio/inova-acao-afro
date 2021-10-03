from django import forms
from django.forms import ModelForm

from peoples.models import People

class PessoaForm(ModelForm):

    class Meta:
        model = People
        fields = '__all__'

