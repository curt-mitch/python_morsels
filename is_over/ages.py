import time
from datetime import datetime

def is_over(age, birthdate):
  today = datetime.today()
  birth_time = datetime.strptime(birthdate, "%Y-%m-%d")
  age_day = birth_time.replace(year=birth_time.year + age)
  return today > age_day
