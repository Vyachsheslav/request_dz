import requests
import json
from pprint import pprint


Hulk = requests.get('https://www.superheroapi.com/api.php/2619421814940190/search/Hulk').json()
int_Hulk = int(Hulk['results'][0]['powerstats']['intelligence'])

Captain = requests.get('https://www.superheroapi.com/api.php/2619421814940190/search/Captain').json()
int_Captain = int(Captain['results'][0]['powerstats']['intelligence'])

content_Thanos = requests.get('https://www.superheroapi.com/api.php/2619421814940190/search/Thanos').json()
intel_Thanos = int(content_Thanos['results'][0]['powerstats']['intelligence'])
intel_dict = {'Hulk': int_Hulk, 'Captain america': int_Captain, 'Thanos': intel_Thanos}

print(f'{max(intel_dict)} - самый умный супергерой')