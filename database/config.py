from pymongo import MongoClient

client = MongoClient('localhost', 27017)
accidents_db = client['car_accidents']

locations = accidents_db['locations']
accidents = accidents_db['accidents']
injuries = accidents_db['injuries']






