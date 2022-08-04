import requests
import Settings
import json

"""
KRW 잔액 조회
"""
res = requests.get(Settings.server_url + '/v1/accounts', headers=Settings.headers)
recvData = res.json()

def getAllAccounts():
    return recvData

def getBalanceFromCode(code):
    for key in recvData:
        if key['currency'] == code:
            return key['balance']


