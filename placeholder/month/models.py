from django.db import models


class Month(models.Model):
    name = models.CharField(max_length=20)
    amountOfDays = models.IntegerField()
    starting_date = models.IntegerField()

    def __str__(self):
        return self.name