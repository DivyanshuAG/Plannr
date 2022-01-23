import django
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from day.models import Day
from django.urls import reverse


class Event(models.Model): 
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)

    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # REDIRECT THIS SOMEWHERE ELSE LATER PLS
        return reverse("main")