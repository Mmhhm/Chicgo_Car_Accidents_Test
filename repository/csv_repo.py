import csv
from bson.objectid import ObjectId
from service.generic import parse_date
from database.config import locations, accidents, injuries
from service.generic import parse_to_int


def read_csv(csv_path):
    with open(csv_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            yield row


def init_accidents_db():
    if locations.count_documents({}) > 0:
        locations.drop()
    if accidents.count_documents({}) > 0:
        accidents.drop()
    if injuries.count_documents({}) > 0:
        injuries.drop()

    for row in read_csv('./Traffic_Crashes_-_Crashes - 20k rows.csv'):
        if not locations.find_one({'location_id': row['BEAT_OF_OCCURRENCE']}):
            location = {
                'location_id': row['BEAT_OF_OCCURRENCE']
            }
            locations.insert_one(location)

        location_id = locations.find_one({'location_id': row['BEAT_OF_OCCURRENCE']}, {"_id": 1})['_id']

        date = parse_date(row['CRASH_DATE'])

        accident = {
            'location_id': location_id,
            'date': date,
            'prime_cause': row['PRIM_CONTRIBUTORY_CAUSE'],
            'sec_cause': row['SEC_CONTRIBUTORY_CAUSE']
        }

        accident_id = accidents.insert_one(accident).inserted_id

        injury = {
            'accident_id': accident_id,
            'location_id': location_id,
            'injuries_total': row['INJURIES_TOTAL'],
            'injuries_fatal': row['INJURIES_FATAL']
        }

        injuries.insert_one(injury)

    print('Finished adding data successfully')











