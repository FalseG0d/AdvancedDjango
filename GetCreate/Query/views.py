from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
    order=Order.objects.all()
    context={
        'orders':order,
    }
    return render(request,"index.html",context)

def save(request):
    if(request.method=="POST"):
        obj, created = Order.objects.get_or_create(customer_name=request.POST.get("name"))
        obj.item=request.POST.get("item")
        obj.price=request.POST.get("price")

        obj.save()


    return redirect('/')