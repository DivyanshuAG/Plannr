from django.shortcuts import render
from .models import Month
from day.models import Day
from week.models import Week

from datetime import datetime

# Create your views here.


def monthView(request, name):
    if request.method == 'GET':

        this_month = name.lower().capitalize()  # standardizes the URL
        month_object = Month.objects.get(name=this_month)

        # send necesary data to the template to be rendered
        data = {
            'month': month_object,
            'dates': Day.objects.filter(month=month_object),
            'weeks': Week.objects.filter(month=month_object),
            'currentYear': datetime.now().year,
            'pad_range': range(0, month_object.starting_date+1),
            'days_of_week':['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        }

        return render(request, template_name='month/index.html', context=data)


def dayView(request, name, date):
    if request.method == 'GET':

        this_month = name.lower().capitalize()
        month_object = Month.objects.get(name=this_month)

        data = {
            'specificDay': Day.objects.get(month=month_object, date=date),
            'month': month_object,
        }
        return render(request, 'month/index.html', context=data)
