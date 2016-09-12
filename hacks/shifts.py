import urllib2
import csv
import datetime

# infrastructure variables:
SHIFTS_CSV_URL = 'http://calc.sankey.info/sgmc_shifts.csv'
COLUMN_FIRST_PERSON = 2
TERMS_CSV_URL = 'http://calc.sankey.info/sgmc_start_dates.csv'

# universal facts:
TERM_LENGTH = datetime.timedelta(days=(7*12))

class EtherCalcHelpers:
  @staticmethod
  def get_date_from_cell(cell_contents):
    try: days_since_1900 = int(cell_contents)
    except: return None
    date = datetime.date(1899,12,30) + datetime.timedelta(days=days_since_1900)
    return date

class Shifts:
  @staticmethod
  def get_row_shifts(row):
    '''get shfits cells from full spreadsheet row'''
    return row[COLUMN_FIRST_PERSON:]
  
  @staticmethod
  def parse_header(row):
    '''parse the header row, return a list of staff members in order'''
    return Shifts.get_row_shifts(row)
  
  @staticmethod
  def parse_row(row):
    '''parse all relevant information in a full spreadsheet data row'''
    row_date = EtherCalcHelpers.get_date_from_cell(row[0])
    if row_date == None:
      return None, None
    row_shifts = Shifts.get_row_shifts(row)
    return row_date, row_shifts
  
  @staticmethod
  def is_upcoming(date):
    today = datetime.date.today()
    return date >= today

  @staticmethod
  def is_relevant(date):
    today = datetime.date.today()
    history_buffer = datetime.timedelta(weeks=12)
    return date >= today - history_buffer
  
  @staticmethod
  def is_scheduled(shifts):
    return '1' in shifts
  
  @staticmethod
  def get_scheduled_staff(shifts, all_staff):
    return [y[1] for y in zip(shifts, all_staff) if y[0] == '1']
  
  @staticmethod
  def fetch_schedule(csvfile_override=None):
    f = None
    if csvfile_override is None:
      f = urllib2.urlopen(SHIFTS_CSV_URL)
    else:
      f = open(csvfile_override)
    rows = csv.reader(f)
    first_row = True
    all_staff = []
    all_staff_filtered = []
    data = {}
    for row in rows:
      if first_row:
        all_staff = Shifts.parse_header(row)
        all_staff_filtered = [x for x in all_staff if len(x) > 0]
        first_row = False
      else:
        date, shifts = Shifts.parse_row(row)
        if not date: break
        shifts_filtered = [x for i, x in enumerate(shifts) if len(all_staff[i]) > 0]
        data[date] = shifts_filtered
    return {
      'all_staff': all_staff,
      'data': data,
    }

class Terms:
  @staticmethod
  def fetch_terms():
    f = urllib2.urlopen(TERMS_CSV_URL)
    rows = csv.reader(f)
    data = {}
    for row in rows:
      member = row[0]
      if len(member) != 0:
        date = EtherCalcHelpers.get_date_from_cell(row[1])
        if date:
          data[member] = date
    return data

  @staticmethod
  def current_term_start(start_date):
    tmp_date = start_date
    while datetime.date.today() > tmp_date + TERM_LENGTH:
      tmp_date += TERM_LENGTH
    return tmp_date

