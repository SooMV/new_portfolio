from django import forms
from django.contrib.auth.forms import UserCreationForm
from Accounts.models import Customer
from django.contrib.auth import authenticate
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400  focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'
        })
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'
        })
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'
        })
    )
    captcha = ReCaptchaField(widget=ReCaptchaV3())
    
    accept_terms = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={
            'class': 'rounded-sm'
        })
    )

    class Meta:
        model = Customer
        fields = ['email', 'password1', 'password2', 'captcha', 'accept_terms']

class UserLoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'
        })
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'
        })
    )
    captcha = ReCaptchaField(widget=ReCaptchaV3())

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("L'adresse e-mail ou le mot de passe est incorrect.")
        return cleaned_data