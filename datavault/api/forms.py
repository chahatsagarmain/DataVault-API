from django import forms
from .models import Users

class LoginForm(forms.ModelForm):
    
    class Meta:
        model = Users
        fields = ['email','password']
    
        
class RegisterForm(forms.ModelForm):
    
    class Meta:
        model = Users
        fields = ['email','username','password']