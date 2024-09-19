import requests

RIOT_API_KEY = 'RGAPI-098d7446-cb7c-42c7-988f-525417869b6f'
GAME_NAME = 'ChestDaysOnly'
TAG_LINE = 'NA1'

url = f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{GAME_NAME}/{TAG_LINE}'
headers = {'X-Riot-Token': RIOT_API_KEY}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(response)