#!/usr/bin/python2
from shifts import Terms
from shifts import TERM_LENGTH
import json
import datetime
terms = Terms.fetch_terms()
data = {}
for member, join_date in terms.iteritems():
  data[member] = {}
  data[member]['start_date'] = join_date.strftime('%F')
  data[member]['previous_term']  = (Terms.current_term_start(join_date) - TERM_LENGTH).strftime('%F')
  data[member]['current_term']   = Terms.current_term_start(join_date).strftime('%F')
  data[member]['next_term']      = (Terms.current_term_start(join_date) + TERM_LENGTH).strftime('%F')
  data[member]['next_next_term'] = (Terms.current_term_start(join_date) + 2*TERM_LENGTH).strftime('%F')
print json.dumps(data)
