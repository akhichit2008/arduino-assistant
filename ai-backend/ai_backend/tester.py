import requests

url = "https://fantastic-couscous-49wgvjq9645hjg44-5000.app.github.dev/"
data = {"action":"getWeather"}

x = requests.post(url,json=data)
print(x.text)