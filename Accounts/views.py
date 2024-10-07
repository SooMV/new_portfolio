from django.shortcuts import render

from Accounts.forms import UserLoginForm, UserRegistrationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import get_user_model, login, logout , authenticate

import logging

# Create your views here.
logger = logging.getLogger(__name__)
User = get_user_model()

def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            if not form.cleaned_data['accept_terms']:
                messages.add_message(request, messages.ERROR, "Vous devez accepter les conditions d'utilisation et la politique de confidentialité pour créer un compte.")
                return render(request, 'accounts/signup.html', {'form': form})
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            captcha_response = form.cleaned_data.get('captcha')

            if User.objects.filter(email=email).exists():
                messages.add_message(request, messages.ERROR, "Ce compte existe déjà.")
            elif captcha_response:
                user = User.objects.create_user(email=email, password=password)
                print(user.email)
                login(request, user)
                logger.info(f"New user {user.email} signed up and logged in.")
                return redirect('index')
            else:
                messages.add_message(request, messages.ERROR, "Le test reCAPTCHA a échoué. Veuillez réessayer.")
        else:
            messages.add_message(request, messages.ERROR, "Les informations fournies sont invalides.")
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/signup.html', {'form': form})

def login_user(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Le compte n'existe pas ou les informations de connexion sont incorrectes")
    else:
        form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': form})
     

def logout_user(request):
    logout(request)
    return redirect('index')