import requests
from lxml import etree
from io import StringIO

def getPage(url):
  response = StringIO(requests.get(url).text)
  return etree.parse(response, etree.HTMLParser())

tree = getPage('https://online-go.com/tournament/49268')
url = tree.xpath('//a[starts-with(@href, "/game/")]/@href')
print(url)