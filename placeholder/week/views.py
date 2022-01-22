from django.shortcuts import render
from week.models import Week

# Create your views here.

def weekView(request, week):
    if request.method == 'GET':
        weekNumber = week
        specificWeek = Week.objects.get(pk=weekNumber)

        data = {
            'specificWeek': specificWeek 
        }
        return render(request,'month/index.html', context=data)
        