from django.shortcuts import render
from .models import Product
from django.db.models import F

# Create your views here.
def home(request):
    Product.objects.update(price=F('price')*1.2)
    products=Product.objects.all()

    context={
        'products':products,
    }

    return render(request,"index.html",context)