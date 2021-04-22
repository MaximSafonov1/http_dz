from pprint import pprint
import requests

url_1 = 'https://www.superheroapi.com/api.php/2619421814940190/search/Hulk'
resp_1 = requests.get(url_1)
data_1 = resp_1.json()
for item_1 in data_1['results']:
  if item_1['name'] == 'Hulk':
    hulk_intelligence = int(item_1['powerstats']['intelligence'])


url_2 = 'https://www.superheroapi.com/api.php/2619421814940190/search/Captain America'
resp_2 = requests.get(url_2)
data_2 = resp_2.json()
for item_2 in data_2['results']:
  if item_2['name'] == 'Captain America':
    captain_intelligence = int(item_2['powerstats']['intelligence'])


url_3 = 'https://www.superheroapi.com/api.php/2619421814940190/search/Thanos'
resp_3 = requests.get(url_3)
data_3 = resp_3.json()
for item_3 in data_3['results']:
  if item_3['name'] == 'Thanos':
    thanos_intelligence = int(item_3['powerstats']['intelligence'])

print(f'Интеллект Халка = {hulk_intelligence}')
print(f'Интеллект Капитана Америки = {captain_intelligence}')
print(f'Интеллект Таноса = {thanos_intelligence}')

the_smartest = {'Hulk': hulk_intelligence, 'Captain America': captain_intelligence, 'Thanos': thanos_intelligence}

print(f'Самый умный из героев это - {max(the_smartest, key=the_smartest.get)}')