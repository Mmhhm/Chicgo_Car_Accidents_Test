from database.config import locations, accidents
from bson.objectid import ObjectId


def accidents_by_location(location: int):
    location_id = locations.find_one({'location_id': location}, {'location_id': 0})
    print(accidents.find({'location_id': location}))
    all_accidents = accidents.count_documents({'location_id': location_id['_id']})
    return all_accidents



def get_accidents_by_cause(location: int):
    location_id = locations.find_one({'location_id': location}, {'location_id': 0})['_id']
    res = accidents.aggregate([{ "$match" : {"location_id" : location_id}},{ "$group" : { "_id" : "$prime_cause", "total" : { "$sum" : 1 } }}])
    return res











