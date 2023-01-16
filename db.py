import pymongo

myclient = pymongo.MongoClient("mongodb+srv://jackson:IM880319@immortal-free.rxzaq.mongodb.net/?retryWrites=true&w=majority") 
db = myclient["myFirstDatabase"]
##連接至database底下的collection 


#for item in collection_name.find():
#   print(item['name'])



def del_space(col_na):
    space = {'name':''}
    sex_space = {'sex':''}
    col_na.delete_many(space)
    col_na.delete_many(sex_space)

def del_someone(col_name, name):
    tmp = {'name' : name , 'sex' : '女'}
    col_name.delete_one(tmp)
    print("成功刪除"+ name)

del_someone(db.light, '張孟淳')
#del_space(db.light)
    


