import requests
import json
import math


# home = requests.get('https://online-go.com/api/v1/tournaments/?page_size=100')

board_size = 9 # could be 11 also

def tournament_count():
  page = requests.get('https://online-go.com/api/v1/tournaments')
  d = json.loads(page.text)
  return d['count']

def get_tournaments(x):
  tournament_data = requests.get('https://online-go.com/api/v1/tournaments/?page_size=100&page={}'.format(x)).text
  return tournament_data

pagetest = open('pagetest.txt', 'w+')
pagecount = math.ceil(tournament_count()/100)
for x in range(1, pagecount+1):
  results = json.loads(get_tournaments(x))['results']
  for y in results:
    if y['board_size'] == board_size:
      tourney_id = y['id']
      print(tourney_id)
      pagetest.write(str(tourney_id) + '\n')
  print('got page {} of {}'.format(x, pagecount))

print('Got all tournament links for board size ' + board_size)
pagetest.close()