import requests
import json
import math
import time
# from lxml import etree
# from io import StringIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
for x in range(1, 2):  # 2 = pagecount+1
  results = json.loads(get_tournaments(x))['results']
  for y in results:
    if y['board_size'] == board_size:
      tourney_id = y['id']
      print('tournament: ' + str(tourney_id))
      tourney_ids.append(tourney_id)
  print('got page {} of {}'.format(x, pagecount))

game_ids = []
pagetest = open('pagetest.txt', 'w')
for touney_id in tourney_ids:
  print('searching for games in tourney id {}'.format(tourney_id))
  options = webdriver.ChromeOptions()
  options.add_argument('--headless')
  options.add_argument('--no-sandbox')
  driver = webdriver.Chrome(options=options)
  driver.get('https://online-go.com/tournament/{}'.format(str(tourney_id)))
  time.sleep(5)
  x = driver.find_elements_by_xpath('//a[starts-with(@href, "/game/")]')
  for y in x:
    game_id = y.get_attribute('href').split('/')[-1]
    game_ids.append(game_id)
    pagetest.write('game_id' + '\n')
    print('game: {}'.format(game_id))
  driver.quit()


pagetest.close()
print('Got all tournament links for board size ' + str(board_size))
