from django.shortcuts import render,redirect
from .models import Record

# Create your views here.
def home(request):
    '''
    records=Record.objects.filter(name="Apoorv")
    context={
        'records':records,
    }'''
    return render(request,"index.html")

def objects(request):
    record=Record.objects.get(name="Apoorv")
    return redirect(record,permanent=True)

def record(request,pk):
    record=Record.objects.get(id=pk)

    context={
        'record':record,
    }

    return render(request,"record.html",context)