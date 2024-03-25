
from django.forms import ModelForm

from .models import Todo


class TodoForm(ModelForm):
    class Meta:
        fields = ['title', 'memo', 'important']
        model = Todo