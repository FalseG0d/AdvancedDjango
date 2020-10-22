from django.shortcuts import render
from .models import Computer
# Create your views here.
def home(request):
    computers=Computer.objects.gaming()
    
    context={
        'computers':computers,
    }

    return render(request,"index.html",context)