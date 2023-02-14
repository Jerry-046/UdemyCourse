from django.forms import ModelForm,widgets
from .models import Project
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets={
            'title' : forms.TextInput(attrs={'style':'width:140%;''height:20px;','placeholder':'Enter here'}),
            'description' : forms.TextInput(attrs={'style':'width:100%;''height:30px;','placeholder':'Enter here'}),
        }
  