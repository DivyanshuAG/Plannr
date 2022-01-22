from django.shortcuts import render
from .models import Month

# Create your views here.
def monthView(request, name):
    if request.method == 'GET':

        print(name)

        data = {
            'month': Month.objects.get(name=name.lower().capitalize())
        }
    
        return render(request, template_name='month/index.html', context=data)