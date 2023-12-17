from django import forms
from .models import Users , Files

class LoginForm(forms.ModelForm):
    
    class Meta:
        model = Users
        fields = ['email','password']
    
        
class RegisterForm(forms.ModelForm):
    
    class Meta:
        model = Users
        fields = ['email','username','password']
        

class FilesForm(forms.ModelForm):
    
    class Meta:
        model = Files
        fields = '__all__'