from django import forms 
from django.contrib.auth.forms import UserCreationForm as CreationForm 
 
 
 
from .models import User 
 
 
class UserCreationForm(CreationForm):
    
    class Meta: 
        model = User 
        fields = ['email', 'username', 'full_name']
