from django import forms


class LoginForm(forms.Form):
    user = forms.CharField(max_length=180)
    password = forms.CharField(widget=forms.PasswordInput())



