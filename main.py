import requests
import json
import math
from lxml import etree
from io import StringIO


board_size = int(input('What board size do you want? 9 or 13?'))
assert(board_size == int(9) or board_size == int(13)), 'Not 9 or 13!'

def tournament_count():
  page = requests.get('https://online-go.com/api/v1/tournaments')
  d = json.loads(page.text)
  return d['count']

def get_tournaments(x):
  tournament_data = requests.get('https://online-go.com/api/v1/tournaments/?page_size=100&page={}'.format(x)).text
  return tournament_data

tourney_ids = []
pagecount = math.ceil(tournament_count()/100)
for x in range(1, 4):  # pagecount+1
  results = json.loads(get_tournaments(x))['results']
  for y in results:
    if y['board_size'] == board_size:
      tourney_id = y['id']
      print('tournament: ' + str(tourney_id))
      tourney_ids.append(tourney_id)
  print('got page {} of {}'.format(x, pagecount))

def getPage(url):
    response = StringIO(requests.get(url).text)
    return etree.parse(response, etree.HTMLParser())

for tourney_id in tourney_ids:
  tree = getPage('https://online-go.com/tournament/{}'.format(tourney_id))
  '''
  challenge: page renders with scripts after the page is requested... meaning that we'll need an automated browser to access the content iff I can't find an API
  '''
  url = tree.xpath('//a[starts-with(@href, "/game/")]/@href')
  print(url)
  

print('Got all tournament links for board size ' + str(board_size))