import requests

url = "https://v3.football.api-sports.io/leagues"
headers = {
    "x-apisports-key": "9ae543b411d500578e9dca61f4006397"
}

data = requests.get(url, headers=headers).json()

for l in data["response"]:
    if "World Cup" in l["league"]["name"]:
        print(l["league"]["id"], l["league"]["name"])