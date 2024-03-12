from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')

        # Basic validation
        errors = []
        if not username or not email or not password or not password_confirmation:
            errors.append('All fields are required.')
        if password != password_confirmation:
            errors.append('Passwords do not match.')
        try:
            validate_email(email)
        except ValidationError:
            errors.append('Invalid email.')

        if User.objects.filter(username=username).exists():
            errors.append('Username already exists.')

        if User.objects.filter(email=email).exists():
            errors.append('Email is already in use.')

        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'RegisterPage.html', {'username': username, 'email': email})

        # Create the user
        user = User.objects.create(username=username, email=email, password=make_password(password))
        messages.success(request, f'Account created for {username}!')
        return redirect('login')

    return render(request, 'RegisterPage.html')
