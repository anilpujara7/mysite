from django import forms
from django.forms.fields import DateField

from myapp.models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'


