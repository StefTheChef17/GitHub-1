import os
import sqlite3
from flask import flask, reguest, jsonify, json
from flask_cors import CORS

app = Flask(_name_)

@app.route("/")
def index():
  return "Zdravo programeri"


if ___name__=='__main__':
  app.run()
