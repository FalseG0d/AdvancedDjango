from django.shortcuts import render
from .models import Cheese

# Create your views here.
def home(request):
    cheese=Cheese.objects.all()

    cheese_1=cheese.filter(quality=5)
    cheese_2=cheese.select_related('place').filter(quality=5)

    context={
        'cheese_1':cheese_1,
        'cheese_2':cheese_2,
    }
    return render(request,"index.html",context)