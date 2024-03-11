from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect


def custom_logout_view(request):
    # Custom actions before logout here (e.g., logging)
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('login')  # Redirect to login page or another appropriate page
