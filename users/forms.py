from django import forms 
from django.contrib.auth.password_validation import password_validators_help_text_html 
from django.contrib.auth.forms import UserCreationForm as CreationForm 
 
 
 
from .models import User 
 
 
class UserCreationForm(CreationForm): 
    password1 = forms.CharField(max_length=100, validators=[password_validators_help_text_html]) 
    password2 = forms.CharField(max_length=100, validators=[password_validators_help_text_html]) 
 
    class Meta: 
        model = User 
        fields = ['email', 'username', 'full_name']
