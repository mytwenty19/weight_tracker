from datetime import date
import datetime
import dateutil.parser
import csv

# Define a function that converts a date to a string
def date2str(date_obj):
    return date_obj.isoformat()

# Define a function that converts a date string to a date object
def str2date(date_str):
    date_time = dateutil.parser.parse( date_str )
    return date_time.date()


# Define a function that returns a string representing todays date
def today2str():
    today = datetime.date.today()
    return today.isoformat()

# Define a function that writes all days in the year to file
def write_weights_file(year, file_name):
    
    start = datetime.date(year, 1, 1)
    end   = datetime.date(year, 12, 31)
    step  = datetime.timedelta(days=1)

    with open(file_name, 'w') as csvfile:
        day_writer = csv.writer(csvfile)

        while start <= end:
            day_writer.writerow([start.isoformat()] + ['NaN'])
            start += step
    
    