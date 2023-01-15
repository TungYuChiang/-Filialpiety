import pymongo
##連接至創建之環境
myclient = pymongo.MongoClient("mongodb+srv://jackson:IM880319@immortal-free.rxzaq.mongodb.net/?retryWrites=true&w=majority") 
##連接至database
db = myclient["myFirstDatabase"]
##連接至database底下的collection 
collection_member= db["member"]

#for item in collection_name.find():
#   print(item['name'])

item_1 = {
    "name" : "江東諭",
    "BirthDay": "88-03-19",
    "sex" : "男",
    "animal" : "兔子",
    "address" : "彰化縣彰化市彰南路四段300巷33弄4號"
    }
collection_member.insert_one(item_1)