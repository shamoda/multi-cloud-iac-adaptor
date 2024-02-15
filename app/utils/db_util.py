from pymongo import MongoClient
import certifi
from app.const.common_const import DB_CONNECTION_URI, DB_NAME

client = MongoClient(DB_CONNECTION_URI, tlsCAFile=certifi.where())
db = client.get_database(DB_NAME)