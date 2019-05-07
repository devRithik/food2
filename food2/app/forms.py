from django import forms


class SignUpForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()


class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

