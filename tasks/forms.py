from django import forms
from django.forms import ModelForm 

from tasks.models import Task

class TaskForm(forms.ModelForm):  #Type ModelForm for shortcut
    
    class Meta:
        model = Task #Same name as the model we want to create the form for
        fields = '__all__' #Allow all fields

