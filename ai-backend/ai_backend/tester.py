import requests

url = "https://fantastic-couscous-49wgvjq9645hjg44-5000.app.github.dev/"
data = {"action":"general","query":"which is the tallest building in the world ?"}

x = requests.post(url,json=data)
print(x.text)