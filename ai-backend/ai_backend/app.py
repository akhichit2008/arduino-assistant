from flask import Flask, g,request,jsonify
from flask_restful import Resource,Api
from data_service import *
import json
import os
import re

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
              if "\u00b0C" in res:
                 res = re.sub("\u00b0C","celsius",res)
              return res
            elif data['action'] == "general":
              res = generalResponse(data['query'])
              return res
            elif data['action'] == "newsHeadlines":
               if data['category']:
                  res = get_headlines(data['category'])
                  return res
               else:
                  return {"Error":"Please provide a news headlines category"}
            else:
             return data

api.add_resource(MakeLLMReq,'/')

if __name__ == "__main__":
    app.run(debug=True)