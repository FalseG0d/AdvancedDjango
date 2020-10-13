from django.shortcuts import render
from .models import Employee

# Create your views here.
def home(request):
    high_Exp_Score=Employee.objects.filter(exp_score=5)
    sec_Dept=Employee.objects.filter(dept="Security")

    high_Exp_Employee=high_Exp_Score|sec_Dept
    context={
        'high_Exp':high_Exp_Employee,
    }
    return render(request,"index.html",context)