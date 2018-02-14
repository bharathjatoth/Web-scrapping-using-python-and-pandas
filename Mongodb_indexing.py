#this assumes that you already running the mongodb on your machine 

from pymongo import MongoClient
import pymongo
import Parser_word  # we import the word parser which extracts the text from word docs and we store it in the mongodb
list1 = Parser_word.parse_word()
# print(list1)
c = MongoClient('localhost',8000) #you can specify your own server adddress
db1 = pymongo.MongoClient().bulk_example
# db1.test.insert(({'i': list1[i]} for i in range(len(list1))))
print(db1.test.count())
for post in range(db1.test.count()):
    print(db1[post])
