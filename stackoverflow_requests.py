import requests

from datetime import datetime, timedelta


current_date = datetime.today().date()
past_date = datetime.now().date() - timedelta(days=1)

response = requests.get(
    'https://api.stackexchange.com/docs/questions',
    params={"todate": past_date, "order": "desc", "max": current_date, "sort": "activity", "tagged": "Python", "filter": "default", "site": "stackoverflow", "run": "true"},
    # headers={'Accept': 'application/json; charset=utf-8', 'User-Agent': 'Accept-Encoding'}
    headers={'Accept-Encoding': 'gzip'}
)

response.raise_for_status()
# data = response.json()
# print(data)
print(response.text)

# for file in data["items"]:
#     print(file["title"])