import django
from django.db import models
from day.models import Day 
from datetime import datetime
from django.contrib.auth.models import User

from django.urls import reverse


class Event(models.Model): 
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)

    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    dates_affected = models.ManyToManyField(Day)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # REDIRECT THIS SOMEWHERE ELSE LATER PLS
        return reverse("main")