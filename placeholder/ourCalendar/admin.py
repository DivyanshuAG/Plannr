from django.contrib import admin
from event.models import Event
from month.models import Month
from week.models import Week
from day.models import Day


admin.site.register(Event)
admin.site.register(Month)
admin.site.register(Week)
admin.site.register(Day)
# Register your models here.
