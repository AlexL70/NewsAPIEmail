import requests as req
import os, email.mime.text as mimetext, email.mime.message as mimemessage
from send_email import send_email

SEARCH_LANG="en"
PAGE_SIZE=20
SEARCH_STRING="israel"
SEARCH_DATE="2024-10-18"
NEWSAPI_KEY = os.environ.get("NEWSAPI_KEY")
URL = f"https://newsapi.org/v2/everything?q={SEARCH_STRING}&from={SEARCH_DATE}" \
    f"&language={SEARCH_LANG}&pageSize={PAGE_SIZE}" \
    f"&sortBy=publishedAt&apiKey={NEWSAPI_KEY}"

r = req.get(URL)
content = r.json()
if (content['status']) != "ok":
    print(f"Error: {content['message']}")
    exit(1)
email_subject: str = f"News from newsapi.org for \"{SEARCH_STRING}\" on {SEARCH_DATE}"
email_content: str = f""
for article in content['articles']:
    article_line: str = f"Title: <a href=\"{article['url']}\">{article['title']}</a><br>{article['description']}<br>By: {article['author']}"
    email_content += f"{article_line}<br><br>"

text = mimetext.MIMEText(email_content, "html")
text["Subject"] = email_subject

send_email(message=text.as_string().encode("utf-8"))

