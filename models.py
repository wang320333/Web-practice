from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/demo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Demo(db.Model):
    __tablename__ = 'demo'
    name = db.Column(db.String(100), primary_key=True)


class User(db.Model):
    __tablename__ = 'user'
    username = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100), primary_key=True)
