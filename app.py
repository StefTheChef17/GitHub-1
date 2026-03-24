import os
import sqlite3
from flask import Flask, reguest, jsonify, json
from flask_cors import CORS

app = Flask(__name__)

@app.route("/")
def index():
  return "Zdravo programeri"


 if ___name__ == '__main__':
   app.run()
