import os
import datetime


from pymongo import MongoClient
from flask import Flask
from flask import request
from flask import flash
from flask import jsonify
from flask import json
from flask import Response
from flask_pymongo import PyMongo


mongo_host = 'localhost'
mongo_port = '27017'
mongo_db_name = 'spark_app'

app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://' + mongo_host + ':' + mongo_port + '/' + mongo_db_name
mongo = PyMongo(app)

@app.route('/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user():
  if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')   
    email = request.form.get('email')
    created_at = updated_at = datetime.datetime.utcnow().isoformat()
    user = { "username": username, "password": password, "email": email, "created_at": created_at ,"updated_at": updated_at } 
    users = mongo.db.user.insert_one(user)
    response = app.response_class(response=json.dumps(user), status=200,mimetype='application/json')
    print response
  
  elif request.method == 'GET':
    
  elif request.method == 'PUT':
    
  elif request.method == 'DELETE':  
    
  else:
    return response

@app.route('/job', methods=['GET', 'POST', 'DELETE'])
def job():
  
  return 0

@app.route('/login', methods=['POST'])
def login():
  return 0

@app.route('/logout', methods=['POST'])
def logout():
  return 0

if __name__ == '__main__':
  app.run(debug=True)
