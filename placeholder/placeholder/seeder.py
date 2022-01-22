# make this populate the calendar with 
# months
# weeks
# days
# import calendar
# DJANGO_SETTINGS_MODULE=settings
from calendar import monthrange
import datetime
import django
from django.conf import settings
settings.configure()
django.setup()

from month.models import Month

# n = calendar.Calendar().itermonthdates(2022, 1)

# for i in n:
#     print(i)

month = ['January','February','March','April','May','June', 'July', 'August', 'September', 'October', 'November', 'December']



for i in month:
    cy = datetime.datetime.now().year
    monthIndex = month.index(i)+1
    monthData = monthrange(cy, monthIndex)
    startDate, daysInMonth = monthData

    m = Month()
    m.name = i
    m.amountOfDays = daysInMonth
    m.starting_date = startDate
    m.save()
