import pymongo
##連接至創建之環境
myclient = pymongo.MongoClient("mongodb+srv://jackson:IM880319@immortal-free.rxzaq.mongodb.net/?retryWrites=true&w=majority") 
##連接至database
db = myclient["myFirstDatabase"]
##連接至database底下的collection 


#for item in collection_name.find():
#   print(item['name'])
memberlist_boy = []
memberlist_girl = []
exe = []

#刪除空白

def del_space(col_na):
    space = {'name':''}
    sex_space = {'sex':''}
    col_na.delete_one(space)
    col_na.delete_one(sex_space)

del_space(db.light)
    

db.light.update_many({}, {"$set":{'light': "光明燈" }})
count = 0
for item in db.light.find():
    count += 1
    if item['light'] == '光明燈':
        print(item)
print(count)
