from django.shortcuts import render, redirect
from .models import Month
from day.models import Day
from week.models import Week

from datetime import datetime

month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']




def monthView(request, name):
    if request.method == 'GET':
        this_month = name.lower().capitalize() # standardizes the URL
        month_object = Month.objects.get(name=this_month)

        try:
            previous_month = month_names[month_names.index(this_month)-1]
        except:
            previous_month = 'December'

        try:
            next_month = month_names[month_names.index(this_month)+1]
        except:
            next_month = 'January'

        previous_month_object = Month.objects.get(name=previous_month)
        
        data = {
            # send necesary data to the template to be rendered
            'month': month_object,
            'dates': Day.objects.filter(month=month_object),
            'weeks': Week.objects.filter(month=month_object),
            'currentYear': datetime.now(),
            'pad_range': range(previous_month_object.amountOfDays - month_object.starting_date, previous_month_object.amountOfDays+1),
            'days_of_week':['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
            'prev_month': previous_month,
            'next_month': next_month

        }

        return render(request, template_name='month/index.html', context=data)


def dayView(request, name, date):
    if request.method == 'GET':

        this_month = name.lower().capitalize()
        month_object = Month.objects.get(name=this_month)

        data = {
            'specificDay': Day.objects.get(month=month_object, date=date),
            'month': month_object,
            'dates': Day.objects.filter(month=month_object),
            'weeks': Week.objects.filter(month=month_object),
        }
        return render(request,'month/index.html', context=data)
        
def autoMonthRedirect(request):
    current_month = month_names[datetime.now().month -1] 

    return monthView(request, current_month)
