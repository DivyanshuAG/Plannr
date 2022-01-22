from django.shortcuts import render
from .models import Month

# Create your views here.
def monthView(request):
    if request.method == 'POST':
        data = {
            'data': Month.objects.all()
        }
        return render(request, template_name='month/index.html', data=data)