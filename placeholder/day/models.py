from django.db import models
from month.models import Month
from week.models import Week
# Day Models

class Day(models.Model):
    date = models.IntegerField(default=1)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.date) +'. of ' + str(self.month)