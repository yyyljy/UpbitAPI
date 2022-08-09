from email import header
import requests
import Settings
import json
import Urls

headers = {"Accept": "application/json"}

"""
일(DAY) 캔들
"""

def getDayCandle(market):
    url = str(Urls.getDaysURL()) + "?market=" + market + "&count=1"
    response = requests.get(url, headers=headers)
    return json.loads(response.text)

def getDayCandles(market,count):
    url = str(Urls.getDaysURL()) + "?market=" + market + "&count=" + count
    response = requests.get(url, headers=headers)
    return json.loads(response.text)

def getDayCandlesTo(market,to,count):
    url = str(Urls.getDaysURL()) + "?market=" + market + "&to=" + to + "&count=" + count
    response = requests.get(url, headers=headers)
    return json.loads(response.text)

"""
Ticker
"""
def getTicker(market):
    url = Urls.getTickerURL() + "?markets=" + market
    response = requests.get(url, headers=headers)
    return response.json()[0]
