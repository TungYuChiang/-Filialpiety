from flask import Flask, render_template, request, redirect, url_for
import pymongo

app = Flask(__name__)
app.config.from_pyfile('config.py')
#data base initial
myclient = pymongo.MongoClient(app.config['MONGO_URL']) 
db = myclient["myFirstDatabase"]


@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

#列印功能
@app.route("/printer/<gender>/<light_type>")
def printer(gender, light_type):
    memberlist = []
    
    for item in db.light.find():
        if (gender == 'boy' and item['sex'] == '男') or \
           (gender == 'girl' and item['sex'] == '女'):
            if light_type == 'light' and item['light'] == '光明燈':
                memberlist.append(item)
            elif light_type == 'money' and item['light'] == '財神燈':
                memberlist.append(item)
    
    template_name = "printer.html" if light_type == 'light' else "printer_m.html"
    
    return render_template(template_name, members=memberlist)

@app.route('/table')
def table():
    memberlist = []
    for item in db.light.find():
        memberlist.append(item)
    return render_template("tables.html", members = memberlist) 

#註冊
@app.route('/register', methods=["POST","GET"])
def register():
    if request.method == "POST":

        name = request.form.get("name")
        birthday = request.form.get("birthday")
        address = request.form.get("address")
        sex = request.form.get("sex")
        light = request.form.get("light")

        item = {
            "name" : name,
            "birthday" : birthday,
            "address" : address,
            "sex" : sex,
            "light" : light
        }

        db.light.insert_one(item)

        return render_template("register.html")
    else:
        return render_template("register.html") 


if __name__ == '__main__':
    #定義app在8080埠運行
    app.run(host="localhost",port=8000)
