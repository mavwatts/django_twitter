from django import forms

class LoginForm(forms.Form):    
    username = forms.CharField(max_length=240, initial="")    
    password = forms.CharField(widget=forms.PasswordInput, initial="")