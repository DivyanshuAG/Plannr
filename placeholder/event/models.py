import django
from django.db import models
from day.models import Day 
from datetime import datetime
from django.contrib.auth.models import User


class Event(models.Model): 
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    dates_affected = models.ManyToManyField(Day)