from pymongo import MongoClient
import pprint

MONGO_URI = "mongodb+srv://admin:admin@cluster0-qvpho.mongodb.net/test?retryWrites=true&w=majority"


def db_connect(MONGO_URI, db_name, col_name):
    client = MongoClient(MONGO_URI)
    database = client[db_name]
    collection = database[col_name]
    return collection


def db_insert_user(collection, user):
    return collection.insert_one(user)


def db_find_all(collection, query={}):
    return collection.find(query)

def db_delete_one(collection, query):
	return collection.delete_one(query)

if __name__ == '__main__':
    print("MongoClient imported successfully!")

#client = MongoClient(MONGO_URI)
#db = client['mi_app']
#users = db['users']

# print("---------------------------------------------------")
# x = db_find_all(users, {"Name": "David Pedroza"})
# y = db_find_all(users, {"Name": "Dav"})

# db.user.find({"Name":"David Pedroza"}).ReadConcern("local")

# #print(x.readConcern())
