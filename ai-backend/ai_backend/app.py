from flask import Flask,request,jsonify
from flask_restful import Resource,Api
from gemini_service import *
import json

app = Flask(__name__)
api = Api(app)

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
            else:
             return data

api.add_resource(MakeLLMReq,'/')

if __name__ == "__main__":
    app.run(debug=True)