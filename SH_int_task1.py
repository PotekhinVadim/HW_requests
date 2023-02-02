import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)

def get_hero_intelligence(name):
    for hero in response.json():
        if hero['name'] == name:
            return hero['powerstats']['intelligence']

heroes_list = ['Hulk', 'Captain America', 'Thanos']
rate_intelligence = []
for hero in heroes_list:
    rate_intelligence.append([get_hero_intelligence(hero), hero])
rate_intelligence.sort()
print(f'Самый умный супергерой {rate_intelligence[-1][1]}')