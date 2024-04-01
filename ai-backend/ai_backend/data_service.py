import google.generativeai as genai
import requests
import sys
import json
from newsapi import NewsApiClient
import pycountry
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



def analyseReport():
    response = model.generate_content(f"Summarise the weather in a single sentence from the given json weather report without including too much scientific data (include only what is required for a common person) : {getWeather()}")
    return response.text


def generalResponse(query):
    response = model.generate_content(query)
    return response.text


'''
News By Categories (List of Topics):

1.Business
2.Entertainment
3.General
4.Health
5.Science
6.Technology
'''


news_api_key = keys["NEWS_API_KEY"]

newsapi = NewsApiClient(api_key=news_api_key)


input_country = "India"
input_countries = [f'{input_country.strip()}']
countries = {}

for country in pycountry.countries:
	countries[country.name] = country.alpha_2

codes = [countries.get(country.title(), 'Unknown code')
		for country in input_countries]

def get_headlines(option):
	data = []
	top_headlines = newsapi.get_top_headlines(

	category=f'{option.lower()}', language='en', country=f'{codes[0].lower()}')
	Headlines = top_headlines['articles']
	if Headlines:
		for articles in Headlines:
			b = articles['title'][::-1].index("-")
			if "news" in (articles['title'][-b+1:]).lower():
				data.append(f"{articles['title'][-b+1:]}: {articles['title'][:-b-2]}.")
			else:
				data.append(f"{articles['title'][-b+1:]} News: {articles['title'][:-b-2]}.")
	else:
		return False
	return data
