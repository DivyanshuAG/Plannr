from django.db import models
from day.models import Day 

class Event(models.Model): 
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    dates_affected = models.ManyToManyField(Day)
    
    def __init__(self):
        