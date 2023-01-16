from flask import Flask, render_template, request, redirect, url_for
import pymongo

app = Flask(__name__)

#data base initial
myclient = pymongo.MongoClient("mongodb+srv://jackson:password@immortal-free.rxzaq.mongodb.net/?retryWrites=true&w=majority") 
db = myclient["myFirstDatabase"]




@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

#列印男生光明燈
@app.route("/printer_boy_light")
def printer():
    memberlist = []
    for item in db.light.find():
        if(item['sex'] == '男' and item['light'] == '光明燈'):
            memberlist.append(item)
    return render_template("printer.html", members = memberlist)
#列印女生光明燈
@app.route("/printer_girl_light")
def printer_g():
    memberlist = []
    for item in db.light.find():
        if(item['sex'] == '女' and item['light'] == '光明燈'):
            memberlist.append(item)
    return render_template("printer.html", members = memberlist)

#列印男生財神燈
@app.route("/printer_boy_money")
def printer_b_m():
    memberlist = []
    for item in db.light.find():
        if(item['sex'] == '男' and item['light'] == '財神燈' ):
            memberlist.append(item)
    return render_template("printer.html", members = memberlist)

#列印女生財神燈
@app.route("/printer_girl_money")
def printer_g_m():
    memberlist = []
    for item in db.light.find():
        if(item['sex'] == '女' and item['light'] == '財神燈'):
            memberlist.append(item)
    return render_template("printer.html", members = memberlist)


@app.route('/table')
def table():
    memberlist = []
    for item in db.light.find():
        memberlist.append(item)
    return render_template("tables.html", members = memberlist) 

@app.route('/register', methods=["POST","GET"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        address = request.form.get("address")
        sex = request.form.get("sex")
        print("name : " + name)
        print("接收成功")
        item = {
            "name" : name,
            "age" : age,
            "address" : address,
            "sex" : sex
        }
        collection_member.insert_one(item)
        return render_template("register.html")
    else:
        return render_template("register.html") 

@app.route('/name', methods=["POST","GET"])
def name():
    if request.method == "POST":
        name_1 = request.form.get("name_1")
        sex_1 = request.form.get("sex_1")
        name_2 = request.form.get("name_2")
        sex_2 = request.form.get("sex_2")
        name_3 = request.form.get("name_3")
        sex_3 = request.form.get("sex_3")
        name_4 = request.form.get("name_4")
        sex_4 = request.form.get("sex_4")
        mylist = [
            {"name" : name_1, "sex" : sex_1, 'light' : '財神燈'},
            {"name" : name_2, "sex" : sex_2, 'light' : '財神燈'},
            {"name" : name_3, "sex" : sex_3, 'light' : '財神燈'},
            {"name" : name_4, "sex" : sex_4, 'light' : '財神燈'},
        ]
        db.light.insert_many(mylist)
        print("name_1 : " + name_1)
        print("name_2 : " + name_2)
        print("name_3 : " + name_3)
        print("name_4 : " + name_4)
        print("接收成功")
        return render_template("name.html")
    else :
        return render_template("name.html")


if __name__ == '__main__':
    #定義app在8080埠運行
    app.run(host="localhost",port=8000)
