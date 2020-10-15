from django.shortcuts import render

# Create your views here.
def home(request):
    print(request.path)
    return render(request,"index.html")