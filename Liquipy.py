from os import close
import requests
import csv
import re
from bs4 import BeautifulSoup
import json
import ast
import os
import hashlib

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in


x = requests.get('https://liquipedia.net/counterstrike/Liquipedia:Matches')
soup = BeautifulSoup(x.text, "html.parser")

matches = soup.find_all('table',class_='infobox_matches_content')
games = []
f = open("Upcoming_Games.dat", "r")
try:
	games = json.load(f)
except:
	pass	
f.close()
for match in matches:
			game = {}
			cells = match.find_all('td')
			try:
				game['team1'] = cells[0].find('span',class_='team-template-text').find('a').get('title')			
				game['team2'] = cells[2].find('span',class_='team-template-text').find('a').get('title')
				game['start_time'] = cells[3].find('span',class_="timer-object").get_text()
				game['tournament'] = cells[3].find('div').get_text().rstrip()
				game['score'] = cells[1].get_text().rstrip()
				game['title'] = game['team1'] + " vs " + game['team2'] + " @ " + game['start_time'] 
				hash_object = hashlib.sha1(game['title'].encode())
				hex_dig = hash_object.hexdigest()
				game['id'] = hex_dig
				flag = False
				if "vs" not in game['score']:
				    continue

				if "IEM" in game['tournament']:
				    for i1 in games:
				        if str(game['id']) == str(i1['id']):
				            flag = True
				    if flag != True:
				        games.append(game)
			except AttributeError:
				continue	
			

f = open("Upcoming_Games.dat", "w")
json.dump(games,f)
f.close()




matches = soup.find_all('table',class_='infobox_matches_content')
games=[]
f = open("Completed_Games.dat", "r")
try:
	games = json.load(f)
except:
	pass	
f.close()
for match in matches:
			game = {}
			cells = match.find_all('td')
			try:
				game['team1'] = cells[0].find('span',class_='team-template-text').find('a').get('title')			
				game['team2'] = cells[2].find('span',class_='team-template-text').find('a').get('title')
				game['start_time'] = cells[3].find('span',class_="timer-object").get_text()
				game['tournament'] = cells[3].find('div').get_text().rstrip()
				game['score'] = cells[1].get_text().rstrip()
				
				
				game['title'] = game['team1'] + " vs " + game['team2'] + " @ " + game['start_time'] 
				hash_object = hashlib.sha1(game['title'].encode())
				hex_dig = hash_object.hexdigest()
				game['id'] = hex_dig
				flag = False

				if "vs" in game['score']:
				    continue
				
				scores = game['score'].split(':')
				game['ascore'] = str(scores[0])
				game['bscore'] = str(scores[1])

				if "IEM" in game['tournament']:
				    for i1 in games:
				        if str(game['id']) == str(i1['id']):
				            flag = True
				    if flag != True:
				        games.append(game)
			except AttributeError:
				continue	
			


f = open("Completed_Games.dat", "w")
json.dump(games,f)
f.close()


				
