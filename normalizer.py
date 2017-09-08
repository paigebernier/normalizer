#!/usr/bin/env python
import sys
import csv
import datetime
import pytz

def parse(header, row):
  line = zip(header, row)
  normalized_row = []

  for header, data in line:
    valid = validate_chars(data)

    if header == 'Timestamp':
      timestamp = normalize_timestamp(valid)
      normalized_row.append(timestamp)

    elif header == 'Address':
      address = normalize_address(valid)
      normalized_row.append(address)

    elif header == 'ZIP':
      zipcode = normalize_zip(valid)
      normalized_row.append(zipcode)

    elif header == 'FullName':
      full_name = normalize_fullName(valid)
      normalized_row.append(full_name)

    elif header == 'FooDuration':
      foo_duration = normalize_duration(valid)
      normalized_row.append(foo_duration)

    elif header == 'BarDuration':
      bar_duration = normalize_duration(valid)
      normalized_row.append(bar_duration)

    elif header == 'TotalDuration':
      total_duration = calculate_totalDuration(foo_duration, bar_duration)
      normalized_row.append(total_duration)

    elif header == 'Notes':
      normalized_row.append(valid)

  return normalized_row


def validate_chars(data):
  valid = data.decode('utf-8', 'replace')
  return valid

def normalize_time(data):
  meridiem = data[2].lower()
  time = [ int(string) for string in data[1].split(":") ]
  hour, minute, second = time

  if meridiem[0] == 'p' and hour == 12:
    hour = 12
  elif meridiem[0] == 'p':
    hour = hour + 12
  elif meridiem[0] == 'a' and hour == 12:
    hour = 0

  time = {'hour':hour, 'minute':minute, 'second':second}
  return time

def get_four_digit_year(year):
  if 50 <= year <= 99:
    year = 1900 + year
  else:
    year = 2000 + year
  return year

def normalize_date(data):
  date = [ int(string) for string in data[0].split("/") ]
  month,day,year = date
  year = get_four_digit_year(year)

  date = {'month':month, 'day':day, 'year':year}
  return date

def normalize_timestamp(data):
  data = data.split(" ")
  date = normalize_date(data)
  month,day,year = date['month'], date['day'], date['year']

  time = normalize_time(data)
  hour,minute,second = time['hour'],time['minute'],time['second']

  eastern = pytz.timezone('US/Eastern')
  pacific = pytz.timezone('US/Pacific')
  utc = pytz.timezone('UTC')

  x = datetime.datetime(year, month, day, hour, minute, second)
  utc_time = x.replace(tzinfo=utc)
  eastern_time = eastern.localize(x)
  normalized_time = eastern_time.isoformat()

  return normalized_time

def normalize_address(data):
  return data

def normalize_zip(data):
  if len(data) < 5:
    zipcode = "{:05}".format(int(data))
  else:
    zipcode = data
  return zipcode

def normalize_fullName(data):
  uppercased = data.upper()
  return uppercased

def normalize_duration(data):
  hour, minute, second = data.split(":")
  duration = (int(hour) * 3600) + (int(minute) * 60) + float(second)
  return duration

def calculate_totalDuration(time1, time2):
  totalDuration = time1 + time2
  return totalDuration

def main():
  reload(sys)
  sys.setdefaultencoding("utf-8")

  reader = csv.reader(sys.stdin)
  writer = csv.writer(sys.stdout)
  output = []
  line = 0
  for row in reader:
    if line == 0:
      header = row
    else:
      normalized = parse(header, row)
      output.append(normalized)
    line += 1

  sys.stdout.write(",".join(header))
  writer.writerows(output)

if __name__ == '__main__':
  main()
