from django import forms
from .models import Log

class PostForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ('title','text')
