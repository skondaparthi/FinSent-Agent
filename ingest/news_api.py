
import requests
import pandas as pd
import os
from dotenv import load_dotenv


def find_news():
    load_dotenv()
    API_KEY = os.getenv("NEWS_API_KEY")
    if not API_KEY:
        raise ValueError("NEWS_API_KEY not set in environment or .env file.")

    url = (
        'https://newsapi.org/v2/everything?'
        'q=stock%20market&'
        'from=2025-07-15&'
        'sortBy=popularity&'
        f'apiKey={API_KEY}'
    )

    response = requests.get(url)
    data = response.json()

    articles = pd.DataFrame([
        {
            "source": a["source"]["name"],
            "title": a["title"],
            "description": a["description"],
            "publishedAt": a["publishedAt"]
        }
        for a in data["articles"]
    ])

    articles = articles.dropna()
    return articles

