from django.shortcuts import render
from week.models import Week
from month.models import Month
# Create your views here.

def weekView(request, name, week):
    if request.method == 'GET':
        weekNumber = week

        month = Month.objects.get(name=name.lower().capitalize())
        specificWeek = Week.objects.get(pk=weekNumber)

        data = {
            'specificWeek': specificWeek,
            'month': month
        }
        return render(request,'month/index.html', context=data)
        