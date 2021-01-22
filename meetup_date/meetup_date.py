"""
This week I'd like you to create a function that determines which day of the
month the San Diego Python meetup should be. The San Diego Python meetup is
on the fourth Thursday of the month (ignoring US holidays, during which we
reschedule it).

Your function should accept year and month arguments and should return a
datetime.date object representing the day of the month for the meetup.

>>> meetup_date(2012, 3)
datetime.date(2012, 3, 22)
>>> meetup_date(2015, 2)
datetime.date(2015, 2, 26)
>>> meetup_date(2018, 6)
datetime.date(2018, 6, 28)
>>> meetup_date(2020, 1)
datetime.date(2020, 1, 23)

You can do it with just the datetime module, but this problem can definitely
be a bit tricky.
"""
import calendar
import datetime

def meetup_date(year, month):
  c = calendar.monthcalendar(year, month)
  first_week = c[0]
  fourth_week = c[3]
  fifth_week = c[4]

  if first_week[calendar.THURSDAY]:
    meeting_day = fourth_week[calendar.THURSDAY]
  else:
    meeting_day = fifth_week[calendar.THURSDAY]

  return datetime.date(year, month, meeting_day)
