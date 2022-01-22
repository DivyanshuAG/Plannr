from django.db import models
from month.models import Month
# from week.models import Week
# Day Models
from django.contrib.auth.models import User

from django.urls import reverse



class Day(models.Model):
    date = models.IntegerField(default=1)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    
    #event = models.ForeignKey(Event, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.date) +'. of ' + str(self.month)
    
    def hasEvent(self):
        return True if self.event else False

