from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect

def delete_user(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()  # Will trigger post_delete signal
        return redirect('home')