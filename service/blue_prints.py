from datetime import datetime

from database.config import locations, accidents, injuries
from bson.objectid import ObjectId



def accidents_by_location(location: int):
    location_id = locations.find_one({'location_id': location}, {'location_id': 0})
    print(accidents.find({'location_id': location}))
    all_accidents = accidents.count_documents({'location_id': location_id['_id']})
    return all_accidents


def get_accidents_by_period(location, date, period):
    location_id = locations.find_one({'location_id': location}, {'location_id': 0})['_id']
    parsed_date = datetime.strptime(date, '%d-%m-%Y')
    if period.lower() == 'day':
        res = accidents.find({'location_id': location_id, 'date': parsed_date}, {'_id': 0, 'location_id': 0})
    elif period.lower() == 'month':
        res = accidents.find({'location_id': location_id, 'date': parsed_date}, {'_id': 0, 'location_id': 0})
    return list(res)


def get_accidents_by_cause(location: int):
    location_id = locations.find_one({'location_id': location}, {'location_id': 0})['_id']
    res = accidents.aggregate([{ "$match" : {"location_id" : location_id}},{ "$group" : { "_id" : "$prime_cause", "total" : { "$sum" : 1 } }}])
    return res


def get_accidents_stat(location: int):
    location_id = locations.find_one({'location_id': location}, {'location_id': 0})['_id']
    res = injuries.aggregate([{ "$match" : {"location_id" : location_id}},{ "$group" : { "_id" : None, "sum_injured" : { "$sum" : "$injuries_total" },
                                                                                                                 "sum_killed" : { "$sum" : "$injuries_fatal" } }}])
    return res










