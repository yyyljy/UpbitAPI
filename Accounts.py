import requests
import Settings
import json
import PrintLog

"""
KRW 잔액 조회
"""
res = requests.get(Settings.server_url + '/v1/accounts', headers=Settings.headers)
recvData = res.json()

def getAllAccounts():
    return recvData

def printAllAccounts():
    for acc in recvData:
        PrintLog.pLog(str(acc))

def getBalanceFromCode(code):
    for key in recvData:
        if key['currency'] == code:
            return key['balance']

def getBalanceFromCodeP(code):
    for key in recvData:
        if key['currency'] == code:
            PrintLog.pLog(code + " Balance : " + key['balance'])
            PrintLog.pLog(code + " Locked  : " + key['locked'])
            if float(key['balance']) > 0:
                PrintLog.pLog("return Balance")
                return key['balance']
            else:
                PrintLog.pLog("return Locked")
                return key['locked']

def getAccInfo(code):
    for key in recvData:     
        if key['currency'] == code:
            return key
    return False
