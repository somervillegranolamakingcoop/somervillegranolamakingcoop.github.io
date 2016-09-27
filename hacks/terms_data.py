#!/usr/bin/python2
from shifts import Terms
from shifts import TERM_LENGTH
import json
import datetime
import sys
if len(sys.argv) == 2:
  terms = Terms.fetch_terms(sys.argv[1])
else:
  terms = Terms.fetch_terms()
data = {}
for member, info in terms.iteritems():
  data[member] = {}
  data[member]['shares'] = info['shares']
  data[member]['start_date'] = info['join_date'].strftime('%F')
  data[member]['previous_term']  = (Terms.current_term_start(info['join_date']) - TERM_LENGTH).strftime('%F')
  data[member]['current_term']   = Terms.current_term_start(info['join_date']).strftime('%F')
  data[member]['next_term']      = (Terms.current_term_start(info['join_date']) + TERM_LENGTH).strftime('%F')
  data[member]['next_next_term'] = (Terms.current_term_start(info['join_date']) + 2*TERM_LENGTH).strftime('%F')
print json.dumps(data)
