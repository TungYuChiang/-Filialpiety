from flask import Flask, render_template, request, redirect, url_for
import pymongo

app = Flask(__name__)

#data base initial
myclient = pymongo.MongoClient("mongodb+srv://jackson:IM880319@immortal-free.rxzaq.mongodb.net/?retryWrites=true&w=majority") 
db = myclient["myFirstDatabase"]
collection_member= db["member"]

@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/table')
def table():
    return render_template("tables.html") 

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

if __name__ == '__main__':
    #定義app在8080埠運行
    app.run(host="localhost",port=8000)
