from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room, Message


# prefixing django decorator to authenticate user before showing view
@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'chatroom/rooms.html', {'rooms': rooms}) # add context dictionary to access rooms object in view(hmtl file)


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)  # gets slug field from DB
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'chatroom/room.html', {'room': room, 'messages':messages})