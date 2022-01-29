from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app=Flask(__name__)
app.secret_key="12345"
app.config["MONGO_URI"]="mongodb://localhost:27017/BBDD"
mongo=PyMongo(app)


@app.route('/add',methods=['POST'])
def hello_world():
    _json=request.json
    _name=_json['name']
    _email=_json['email']
    _password=_json['password']
    if _name and _email and _password and request.method=='POST':
        id=mongo.db.BBDD.insert({'name':_name,'email':_email,'password':_password})
        resp=jsonify("Agregado socioo")
        resp.status_code=200
        return resp
    else:
        msj={
            'status':404,
            'message':'Not fount'+request.url,
        }
        resp=jsonify(msj)
        resp.status_code = 404
        return resp

app.run()