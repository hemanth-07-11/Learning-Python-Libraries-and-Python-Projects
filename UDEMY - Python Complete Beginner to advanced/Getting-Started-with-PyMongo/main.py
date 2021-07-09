

from pymongo import MongoClient

my_client = MongoClient()

db = my_client.my_database

users = db.users

user1 = {"username": "hems", "password": "dkdjhg", "fav_number":07, "hobbies": ["aaa", "bbb", "ccc"]}

user_id = users.insert_one(user1).inserted_id

users = [{"username": "user2", "password": "12345"}, {"username": "user3", "password": "23456"}]
Users = db.users
inserted = Users.insert_many(users)
inserted.inserted_ids







