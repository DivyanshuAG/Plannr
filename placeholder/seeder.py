# make this populate the calendar with 
# months
# weeks
# days

from calendar import monthrange
import calendar
import datetime


#NOTE To run this script you need to import it from manage.py shell by using:
# python manage.py shell
# import seeder
# seeder.seed_months()
# etc

# this will populate the months for the calendar.


#import of models

# try and catch for development purposes.
try:
    from month.models import Month
    from week.models import Week
    from day.models import Day
except:
    pass

month = ['January','February','March','April','May','June', 'July', 'August', 'September', 'October', 'November', 'December']

#NOTE calendar.month() <- look at this



def seed_months(remove_all_previous_entries=False):
    """TO NOT PASS THIS 'TRUE' UNLESS YOU KNOW EXACTLY WHAY YOU ARE DOING"""

    weekIter = 0
    dayIter = 0

    def cleaned():
        ###NOTE 
        # only use this if you NEED to remove ALL of the entries
        # use with caution
        Month.objects.all().delete()
        Week.objects.all().delete()
        print('Cleaned')

    if remove_all_previous_entries==True:
        cleaned()

    for i in month:
        cy = datetime.datetime.now().year
        monthIndex = month.index(i)+1
        monthData = monthrange(cy, monthIndex)
        startDate, daysInMonth = monthData

        try:
            # Try anc catch for development purposes.
            # seeding of months
            m = Month()
            m.pk = monthIndex
            m.name = i
            m.amountOfDays = daysInMonth
            m.starting_date = startDate
            m.save()
        except:
            pass



        weekCount = len(calendar.month(cy, monthIndex).split('\n'))-3
        #print(weekCount)

        try:
            # Try anc catch for development purposes.
            # seeding of weeks
            for k in range(1,weekCount+1):
                weekIter += 1
                w = Week()
                w.pk = weekIter
                w.name = k
                w.month = m
                w.save()
        except:
            pass

        try:
            # Try anc catch for development purposes.
            # seeding of days
            for k in range(1, daysInMonth+1):
                dayIter += 1
                d = Day()
                d.pk = dayIter
                d.date = k
                d.month = m
                d.save()

        except:
            pass

if __name__ == '__main__':
    seed_months()