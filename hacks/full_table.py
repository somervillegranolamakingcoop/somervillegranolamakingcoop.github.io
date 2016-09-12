#!/usr/bin/python2
from shifts import Shifts
import json
import sys
if len(sys.argv) == 2:
  schedule = Shifts.fetch_schedule(sys.argv[1])
else:
  schedule = Shifts.fetch_schedule()
new_data = []
for date, shifts in schedule['data'].items():
  if Shifts.is_relevant(date):
    new_data.append({
      'date': date.strftime('%F'),
      'dow': date.strftime('%a'),
      'shifts': shifts,
      'is_scheduled': Shifts.is_scheduled(shifts),
    }) 
schedule['data'] = sorted(new_data, key=lambda y: y['date'])
print json.dumps(schedule)
