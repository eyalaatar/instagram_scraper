from pymongo import MongoClient

class Database:
    def __init__(self, CONNECTION_STRING):
        self.CONNECTION_STRING = CONNECTION_STRING

    def connect(self):
        client = MongoClient(self.CONNECTION_STRING)
        print('Logged into DB')
        return client['instagram']

    def add(self, dic):
        dbname = self.connect()
        doc = dbname['insta']
        x = doc.insert_one(dic)
        print('Added to DB')
