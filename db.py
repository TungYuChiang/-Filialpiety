import pymongo
##連接至創建之環境
myclient = pymongo.MongoClient("mongodb+srv://jackson:IM880319@immortal-free.rxzaq.mongodb.net/?retryWrites=true&w=majority") 
##連接至database
db = myclient["myFirstDatabase"]
##連接至database底下的collection 
collection_member= db["member"]

#for item in collection_name.find():
#   print(item['name'])
memberlist = []
print(type(collection_member.find()))
for item in collection_member.find():
    memberlist.append(item)
for member in memberlist:
    print(member['name'])