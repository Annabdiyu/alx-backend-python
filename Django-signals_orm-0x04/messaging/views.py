'''from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect

def delete_user(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()  # Will trigger post_delete signal
        return redirect('home')'''
        
from django.shortcuts import render
from .models import Message
from django.db.models import Prefetch

def thread_detail(request, message_id):
    # Get the root message and prefetch all replies recursively
    root_message = Message.objects.filter(
        id=message_id
    ).filter(
        models.Q(sender=request.user) | models.Q(receiver=request.user)  # User filtering
    ).select_related(
        'sender', 'receiver'  # Optimize user lookups
    ).prefetch_related(
        Prefetch(
            'replies',
            queryset=Message.objects.select_related('sender', 'receiver')
            .prefetch_related(Prefetch('replies', queryset=Message.objects.all()))
        )
    ).first()

    return render(request, 'messaging/thread.html', {
        'root_message': root_message
    })