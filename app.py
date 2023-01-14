from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/index")
def root():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/table')
def table():
    return render_template("tables.html") 

if __name__ == '__main__':
    #定義app在8080埠運行
    app.run(host="localhost",port=8000,debug=True)
