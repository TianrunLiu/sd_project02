from flask import Flask, redirect, render_template, request

from util import userMethods

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("landing_page.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if (request.method == "POST"):
        username = request.form['username']
        password = request.form['password']
        result = userMethods.checkInfo(username, password)
        print(result)
    return render_template("login.html")

@app.route("/register", methods = ["POST", "GET"])
def register():
    return render_template("register.html")

app.debug=True
app.run()