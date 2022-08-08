from email import message
from genericpath import exists
import jwt
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote

import Urls
import Settings
import PrintLog

"""
## side
bid(매수)
ask(매도)
"""
#주문 가능 정보
def getOrderChance(market):
    params = {'market': market}
    query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': Settings.access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, Settings.secret_key)
    authorization = 'Bearer {}'.format(jwt_token)
    headers = {'Authorization': authorization, }

    res = requests.get(Urls.getOrdersChanceURL(), params=params, headers=headers)
    return res.json()

# 개별 주문 조회
def getOrder(uuidInput):
    params = {'uuid': uuidInput}
    query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': Settings.access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, Settings.secret_key)
    authorization = 'Bearer {}'.format(jwt_token)
    headers = {
    'Authorization': authorization,
    }

    res = requests.get(Urls.getOrderURL(), params=params, headers=headers)
    return res.json()

# 주문 리스트 조회
def getOrdersList():
    params = {'states[]': ['wait']}
    query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': Settings.access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, Settings.secret_key)
    authorization = 'Bearer {}'.format(jwt_token)
    headers = {'Authorization': authorization, }

    res = requests.get(Urls.getOrdersURL(), params=params, headers=headers)
    return res.json()

# 주문 취소 접수
def deleteOrder(uuidInput):
    params = {'uuid': uuidInput}
    query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': Settings.access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, Settings.secret_key)
    authorization = 'Bearer {}'.format(jwt_token)
    headers = {
    'Authorization': authorization,
    }

    res = requests.delete(Urls.deleteOrderURL(), params=params, headers=headers)
    res = res.json()
    try:
        PrintLog.pLog("ERROR : " + res['error']['message'])
        return False
    except:
        return res

# 주문하기
def orderMarketPrice(market, side, volume, price):
    params = {
        'market': market,
        'side': side,
        'ord_type': 'limit',
        'price': price,
        'volume': volume
    }
    query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': Settings.access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, Settings.secret_key)
    authorization = 'Bearer {}'.format(jwt_token)
    headers = {'Authorization': authorization, }

    res = requests.post(Urls.PostOrdersURL(), params, headers=headers)
    res = res.json()
    try:
        PrintLog.pLog("ERROR : " + res['error']['message'])
        return False
    except:
        return res
"""
# 주문취소 접수 Response
{
    'bid_fee':'0.0005',
    'ask_fee':'0.0005',
    'maker_bid_fee':'0.0005',
    'maker_ask_fee':'0.0005',
    'market':{
    'id':'KRW-HUNT',
    'name':'HUNT/KRW',
    'order_types':[
    'limit'
    ],
    'order_sides':[
    'ask',
    'bid'
    ],
    'bid':{
    'currency':'KRW',
    'min_total':5000.0
    },
    'ask':{
    'currency':'HUNT',
    'min_total':5000.0
    },
    'max_total':'1000000000',
    'state':'active'
    },
    'bid_account':{
    'currency':'KRW',
    'balance':'39995.05889148',
    'locked':'0',
    'avg_buy_price':'0',
    'avg_buy_price_modified':True,
    'unit_currency':'KRW'
    },
    'ask_account':{
    'currency':'HUNT',
    'balance':'0',
    'locked':'15.94896331',
    'avg_buy_price':'627',
    'avg_buy_price_modified':False,
    'unit_currency':'KRW'
    }
}
{
    'uuid':'3736be4b-4691-48f3-8500-da50d519b0f5',
    'side':'bid',
    'ord_type':'limit',
    'price':'615',
    'state':'wait',
    'market':'KRW-HUNT',
    'created_at':'2022-08-09T00:51:55+09:00',
    'volume':'16.2601626',
    'remaining_volume':'16.2601626',
    'reserved_fee':'4.9999999995',
    'remaining_fee':'4.9999999995',
    'paid_fee':'0',
    'locked':'10004.9999989995',
    'executed_volume':'0',
    'trades_count':0
}
"""