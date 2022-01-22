from django.contrib import admin
from event.models import Event
from month.models import Month
from week.models import Week
from day.models import Day

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ('title','description', 'owner_id')
    list_display = ('title', 'description')
#admin.site.register(EventAdmin)

@admin.register(Month)
class MonthAdmin(admin.ModelAdmin):
    list_display = ('name','amountOfDays','starting_date')
#admin.site.register(Month)

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('__str__','date','month')
#admin.site.register(Day)

admin.site.register(Week)
# Register your models here.
