from django.shortcuts import render
from .models import Message

def home(request):
    message = Message.objects.first()
    return render(request, "home.html", {"message": message})
