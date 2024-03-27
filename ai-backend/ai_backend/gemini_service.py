import google.generativeai as genai
import requests
import sys
import json

with open("secrets.json","r") as s:
    keys = json.load(s)



gemini_api_key = keys["GEMINI_API_KEY"]
tommorow_io_api_key = keys["TOMMOROWIO_API_KEY"]
url = f'https://api.tomorrow.io/v4/weather/realtime?location=chennai&apikey={tommorow_io_api_key}'
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel("gemini-1.0-pro")

'''
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(model.name)
'''


def getWeather():
    res = requests.get(url)
    if res.status_code == 200:
        return res.text
    else:
        print("Error in fetching weather data!!!!",file=sys.stderr)
        sys.stderr.write("Error in fetching weather data!!!!")
        exit()



def analyseReport():
    response = model.generate_content(f"Summarise the weather in a paragraph by analysing the given json weather report : {getWeather()}")
    return response.text
