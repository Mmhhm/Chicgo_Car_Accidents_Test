from datetime import datetime

def parse_date(date_str: str):
    has_seconds = len(date_str.split(' ')) > 2
    date_format = '%m/%d/%Y'
    curr_date = datetime.strptime(date_str[:10], date_format)
    return curr_date

def parse_to_int(string):
    if string:
        return int(string)
    else:
        return 0

