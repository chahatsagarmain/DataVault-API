from django import forms

class LoginForm(forms.ModelForm):
    
    email = forms.EmailField(required=True,help_text="Enter an email")
    password = forms.CharField(max_length=256,
                                required=True)
    
    