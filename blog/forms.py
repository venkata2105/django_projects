from django import forms


class Registration(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(max_length=15)


class Login(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=15)