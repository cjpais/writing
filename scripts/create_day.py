#! /usr/local/bin/python3

from datetime import datetime
from pathlib import Path

BASE_DIR = "../serve/day/"
DAY_LOOKUP = {
    1: 'jan',
    2: 'feb',
    3: 'mar',
    4: 'apr',
    5: 'may',
    6: 'june',
    7: 'july',
    8: 'aug',
    9: 'sept',
    10: 'oct',
    11: 'nov',
    12: 'dec'
}

DAY_NAME_FORMAT = "%A %B %d, %Y"
DAY_TEMPLATE = "# {}\n"

# get today's date
d = datetime.now()

# create directory with the date
dir_string = "{}{}_{}/".format(DAY_LOOKUP[d.month], d.day, d.year)
day_dir = BASE_DIR + dir_string
Path(day_dir).mkdir(exist_ok=True)

# open a file and write the day
with open(day_dir + "index.md", 'w') as index:
    index.write(DAY_TEMPLATE.format(d.strftime(DAY_NAME_FORMAT)))
