from pymongo import MongoClient

bucket_name = 'my-hive'
client = MongoClient('localhost', 27017)  
db = client['search_engine_db']