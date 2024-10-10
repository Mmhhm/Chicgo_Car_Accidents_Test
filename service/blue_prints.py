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
    str_date = datetime.strptime(date, '%Y-%m-%d')
    curr_date = accidents.find({'location_id': location_id})
    for d in curr_date:
        d['date'] = d['date'].setHours(0,0,0,0)
    if period.lower() == 'day':
        res = curr_date.get('date')
    return list(res)


def get_accidents_by_cause(location: int):
    location_id = locations.find_one({'location_id': location}, {'location_id': 0})['_id']
    res = accidents.aggregate([{ "$match" : {"location_id" : location_id}},{ "$group" : { "_id" : "$prime_cause", "total" : { "$sum" : 1 } }}])
    return res


def get_accidents_stat(location: int):
    location_id = locations.find_one({'location_id': location}, {'location_id': 0})['_id']
    res = injuries.aggregate([{ "$match" : {"location_id" : location_id}},{ "$group" : { "_id" : 0, "sum_injured" : { "$sum" : {"$toInt": "$injuries_total" }},
                                                                                                                      "sum_killed" : { "$sum" : {"$toInt": "$injuries_fatal" } }}}])
    return res









