from django.db import models
from month.models import Month

# Create your models here.
class Week(models.Model):
    name = models.CharField(max_length=30)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' of ' + str(self.month)