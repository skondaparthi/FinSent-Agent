import requests
import pandas as pd

API_KEY = "b72b13eec06c4951b4049d799118efcb"

url = ('https://newsapi.org/v2/everything?'
       'q=stock%20market&'
       'from=2025-07-01&'
       'sortBy=popularity&'
       f'apiKey={API_KEY}')

response = requests.get(url)
data = response.json()

articles = pd.DataFrame([{
    "source": a["source"]["name"],
    "title": a["title"],
    "description": a["description"],
    "publishedAt": a["publishedAt"]
} for a in data["articles"]])


print(articles.head())
print("hello again")

