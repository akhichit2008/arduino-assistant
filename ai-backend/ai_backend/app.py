from flask import Flask, g,request,jsonify
from flask_restful import Resource,Api
from gemini_service import *
import json
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
import jwt
import time
from werkzeug.security import generate_password_hash,check_password_hash
import os

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(15),index=True)
    password_hash = db.Column(db.String(128))

    def hash_password(self,password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
    
    def gen_auth_token(self,expires_in=1200):
        return jwt.encode(
            {'id':self.id,'exp':time.time()+expires_in},app.config['SECRET_KEY'],algorithm='HS256'
        )
    
    @staticmethod
    def verify_auth_token(token):
        try:
            data = jwt.decode(token,app.config['SECRET_KEY'],algorithms=['HS256'])
        except:
            return None
        return User.query.get(data['id'])
    
@auth.verify_password
def verify_password(username_token,password):
    user = User.verify_password(username_token)
    if not user:
        user =User.query.filter_by(username=username_token).first()
        if not user or not user.verify_password(password):
            return False
    
    g.user = user
    return True


class MakeLLMReq(Resource):
    def post(self):
        data = request.get_json()
        print(type(data))
        if not isinstance(data,dict):
             return jsonify({'error':'Invalid Data Format'})
        else:
            if data['action'] == "getWeather":
              res = analyseReport()
              return res
            elif data['action'] == "general":
              res = generalResponse(data['query'])
              return res
            else:
             return data

api.add_resource(MakeLLMReq,'/')

if __name__ == "__main__":
    if not os.path.exists('db.sqlite'):
        db.create_all()
    app.run(debug=True)