from database.config import locations, accidents
from bson.objectid import ObjectId


def accidents_by_location(location: int):
    location_id = locations.find_one({'location_id': location})['_id']
    print(accidents.find({'location_id': location}))
    all_accidents = accidents.count_documents({'location_id': ObjectId(location_id)})
    return all_accidents















