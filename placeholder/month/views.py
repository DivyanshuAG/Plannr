from django.shortcuts import render
from .models import Month
from day.models import Day
from week.models import Week

# Create your views here.
def monthView(request, name):
    if request.method == 'GET':

        
        this_month= name.lower().capitalize() # standardizes the URL
        month_object = Month.objects.get(name=this_month)

        # send necesary data to the template to be rendered
        data = {
            'month': month_object,
            'dates': Day.objects.filter(month=month_object),
            'weeks': Week.objects.filter(month=month_object),
        }
    
        return render(request, template_name='month/index.html', context=data)