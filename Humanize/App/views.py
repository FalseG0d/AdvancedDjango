from django.shortcuts import render
from .models import Record

# Create your views here.
def home(request):
    record=Record.objects.all()

    context={
        'records':record,
    }

    return render(request,"index.html",context)