from django.views.decorators.cache import cache_page
from django.shortcuts import render
from .models import Message  # Or your message model

# Add cache decorator with 60-second timeout
@cache_page(60)  # 60 seconds timeout
def conversation_detail(request, conversation_id):
    # Get conversation messages - this is where you'd normally query messages
    # Example query:
    messages = Message.objects.filter(
        conversation_id=conversation_id
    ).select_related('sender').order_by('timestamp')
    
    return render(request, 'chats/conversation.html', {
        'messages': messages,
        'conversation_id': conversation_id
    })