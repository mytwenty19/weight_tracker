from datetime import date
import datetime
import dateutil.parser
import csv
import pandas as pd


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
    
# Define a function to read weights file as a DataFrame
def read_weights_file(file_name):
    data_frame = pd.read_csv(file_name,header=None, names=['act_weight'],parse_dates=True)
    return data_frame

# Select a part of the data frame
def select_by_date(data_frame, from_date_str, to_date_str):
    from_date = str2date(from_date_str)
    to_date   = str2date(to_date_str)
    step = datetime.timedelta(days=1)

    date_list = []
    while from_date <= to_date:
        date_list.append(from_date)
        from_date += step
    
    return data_frame.loc[date_list]
