from django.shortcuts import render
from week.models import Week

# Create your views here.

def weekView(request, week):
    if request.method == 'get':
        weekNumber = week
        specificWeek = Week.objects.get(pk=weekNumber)

        data = {
            'specificWeek': specificWeek 
        }
        return render('month/index.html', data=data)
        