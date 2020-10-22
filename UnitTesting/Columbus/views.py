from django.shortcuts import render
from .models import Name
from .forms import NameForm

# Create your views here.
def i_was_here(request):
    form=NameForm()

    if request.method=="POST":
        form=NameForm(request.POST)
        if form.is_valid():
            form.save()

    names=Name.objects.all()
    context={
        "names":names,
        "form":form,
    }
    
    return render(request,"index.html",context)