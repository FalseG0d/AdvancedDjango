from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    story=Article.objects.all()

    context={
        'stories':story,
    }

    return render(request,"index.html",context)