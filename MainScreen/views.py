from django.shortcuts import render
from .models import User

def home(request):
    context = {
        'total': User.objects.all()
    }
    return render(request, 'MainScreen/Home.html')