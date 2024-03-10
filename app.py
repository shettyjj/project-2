from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('etheral.html')
@app.route("/add")
def add():
    return render_template("add.html")
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
