from flask import Flask, redirect, url_for, render_template, request
from database import Database

app = Flask(__name__)
db = Database()

@app.route("/")
def home():
    return "Welcome!"

@app.route("/login")
def login(): 
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
