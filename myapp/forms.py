from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Your Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Your Password'}))