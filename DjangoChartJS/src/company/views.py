from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

# Create your views here.

class CompanyChartView(TemplateView):
    template_name='companies/chart.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"]=Company.objects.all()

        return context