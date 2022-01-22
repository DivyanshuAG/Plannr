from django.db import models
from month.models import Month
from week.models import Week
# Day Models

class Day(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)