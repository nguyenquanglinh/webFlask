import pymongo

# Kết nối đến database mongodb
client = pymongo.MongoClient(
    "mongodb://nbhoa:12345678Abc@ds231307.mlab.com:31307/c4e")

# tạo db test 1
db = client.c4e
# db.nbquang.insert_one({"bac":321})
# db.nbquang.insert_one({"name":"quang",'age':10})
# db.nbquang.insert_one({"name":"quan",'age':12})
# db.nbquang.insert_one({"name":"quag",'age':11})
# db.nbquang.update_one({"age":10},{"$set":{"'age":11}})
# a=list(db.nbquang.find({'age':11}))
# print(a)


def add_user(name,age):
    db.nbquang.insert_one({"name":name,'age':age})

def get_all_user():
    return list(db.nbquang.find())

def delete_by_name(name):
    db.nbquang.delete_one({"name":name})
    


