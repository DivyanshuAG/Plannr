from django import forms
from django.contrib.auth.models import User

class EventForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(max_length=299)
    # start_time = forms.DateTimeField()
    # end_time = forms.DateTimeField()

    
