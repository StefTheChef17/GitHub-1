import os
import sqlite3
from flask import flask, reguest, jsonify, json
from flask-cors import CORS

app = Flask(_name_)

@app.route("/")
def index():
  return "Zdravo programeri"


if _name_=='__main__':
  app.run()
