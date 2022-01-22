from django import forms
from django.contrib.auth.models import User
from day.models import Day

#print(Day.objects.all().values)
class EventForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)
    day = forms.DateField()
