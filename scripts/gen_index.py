from datetime import datetime, timedelta
from shutil import copyfile
import os
import bisect
import commonmark

from jinja2 import Template, Environment, FileSystemLoader, select_autoescape

jinja_env = Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape(['html', 'xml'])
)

DAY_LOOKUP = {
  'jan': 1,
  'feb': 2,
  'mar': 3,
  'apr': 4,
  'may': 5,
  'june': 6,
  'july': 7,
  'aug': 8,
  'sept': 9,
  'oct': 10,
  'nov': 11,
  'dec': 12
}

DAY_NAME_FORMAT = "%B %d, %Y"

class Day:

  def __init__(self, date, url, path):
    self.date = date
    self.name = date.strftime(DAY_NAME_FORMAT).replace(" 0", " ")
    self.url = url
    self.path = path

    print

  def __lt__(self, other):
    if self.date < other.date:
      return True
    else:
      return False

class Year:
  def __init__(self, date):
    self.date = date
    self.name = date.year
    self.months = []

  def __lt__(self, other):
    if self.date < other.date:
      return True
    else:
      return False

  def add_month(self, month):
    bisect.insort(self.months, month)

class Month:
  def __init__(self, date, year):
    self.year = year
    self.date = date
    self.name = date.strftime("%B")
    self.days = []

  def __lt__(self, other):
    if self.date < other.date:
      return False
    else:
      return True
  
  def add_day(self, day):
    bisect.insort(self.days, day)

def get_this_week_dates():
  today = datetime.now()
  start = today - timedelta(days=today.weekday())
  end = start + timedelta(days=6)

  return start.date(), end.date()

def get_this_weeks_days(all_days):
  this_week = []

  week_start, week_end = get_this_week_dates()

  for day in all_days:
    if day.date.date() >= week_start and day.date.date() <= week_end:
      this_week.append(day)

  return this_week

def get_all_days():
  days = []

  # TODO FIXME hardcoded path from laziness
  day_dir = "../serve/day"
  day_dirs = next(os.walk(day_dir))[1]

  for raw_day in day_dirs:
    for key, month in DAY_LOOKUP.items():
      if key in raw_day:
        break
    
    path = day_dir + "/" + raw_day
    year = int(raw_day.split("_")[-1])
    day = int(raw_day.split("_")[0].replace(key, ""))
    bisect.insort(days, (Day(datetime(year, month, day), raw_day, path)))
  
  return days

def get_days_past(all_days, this_week):
  years = []
  created_months = {}
  created_years = {}

  days = [x for x in all_days if x not in this_week]

  for day in days:
    # get or create the year
    if day.date.year in created_years:
      year = created_years[day.date.year]
    else:
      year = Year(day.date)
      created_years[day.date.year] = year
      years.append(year)
    
    # get or create the month
    if day.date.month in created_months:
      month = created_months[day.date.month]
    else:
      month = Month(day.date, year)
      created_months[day.date.month] = month
      year.add_month(month)
    
    month.add_day(day)

  return years

if __name__ == "__main__":
  days = get_all_days()
  latest = days[-1]
  copyfile(latest.path + "/index.html", "../serve/today.html")
  #print(days)
  this_week = get_this_weeks_days(days[:-1])

  # get all of the days that are not in this week and return the years
  # so we can use our template
  years = get_days_past(days, this_week)
  yrs_rev = years[::-1]

  # generate .md from template
  template = jinja_env.get_template("index.template")
  output_md = template.render({"latest": latest, "this_week": this_week, "years": yrs_rev})

  #print(output_md)

  html = commonmark.commonmark(output_md)

  template = jinja_env.get_template("base.template")
  output_html = template.render({"content": html, "title": "Daily Notes"})

  with open("../serve/index.html", 'wb') as out_f:
    out_f.write(output_html.encode('utf-8'))
