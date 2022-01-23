from django.shortcuts import render, redirect
from .models import Month
from day.models import Day
from week.models import Week
from event.models import Event

from django.contrib.auth.decorators import login_required


from datetime import datetime

month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

@login_required(login_url='/registration/login/')
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
        
        def getRange():
            remainder = month_object.amountOfDays % 7
            if not remainder and month_object.starting_date == 0:
                return 0
            n = len(range(previous_month_object.amountOfDays - month_object.starting_date, previous_month_object.amountOfDays+1)) + month_object.amountOfDays
            return range(1, 7 - (n % 7) +1)


        def getArrOfEventIds():
            e = Event.objects.all()
            r = []
            for event in e:
                r.append(event.day)

            return r

        def ReturnTodayIfCurrentMonth(current_month):
            if current_month == month_names[datetime.now().month -1]:
                return datetime.now().day
            return None

        data = {
            # send necesary data to the template to be rendered
            'month': month_object,
            'dates': Day.objects.filter(month=month_object),
            'weeks': Week.objects.filter(month=month_object),
            'currentYear': datetime.now(),
            'pad_range': range(previous_month_object.amountOfDays - month_object.starting_date, previous_month_object.amountOfDays+1),
            'days_of_week':['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
            'prev_month': previous_month,
            'next_month': next_month,
            'over_pad_range': getRange(),
            'arr_of_events' : getArrOfEventIds(),
            'today': ReturnTodayIfCurrentMonth(this_month)
        }

        return render(request, template_name='month/index.html', context=data)

@login_required(login_url='/registration/login/')
def dayView(request, name, date):
    if request.method == 'GET':

        this_month = name.lower().capitalize()
        month_object = Month.objects.get(name=this_month)

        today = Day.objects.get(month=month_object, date=date)

        data = {
            'specificDay': Day.objects.get(month=month_object, date=date),
            'month': month_object,
            'dates': Day.objects.filter(month=month_object),
            'weeks': Week.objects.filter(month=month_object),
            'events': Event.objects.filter(day=today.id),
            'currentYear': datetime.now().year
        }
        return render(request,'day/index.html', context=data)
        
@login_required(login_url='/registration/login/')
def inbox(request):
    if request.method == 'GET':

        data = {
            'events': Event.objects.all(),
            'currentYear': datetime.now().year
        }
        return render(request,'day/index.html', context=data)

@login_required(login_url='/registration/login/')      
def autoMonthRedirect(request):
    current_month = month_names[datetime.now().month -1] 

    return monthView(request, current_month)
