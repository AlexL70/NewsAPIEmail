import requests as req
import os

NEWSAPI_KEY = os.environ.get("NEWSAPI_KEY")
URL = f"https://newsapi.org/v2/everything?q=israel&from=2024-09-19&sortBy=publishedAt&apiKey={NEWSAPI_KEY}"

r = req.get(URL)
content = r.json()
print(content['status'])
print(content['totalResults'])
for article in content['articles']:
    print(article['title'])
