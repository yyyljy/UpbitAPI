import imp
from ssl import ALERT_DESCRIPTION_ACCESS_DENIED
from tkinter.filedialog import SaveFileDialog
import requests
from urllib.parse import urlencode, unquote
import json
import time
import pyupbit
import datetime

"""
구현 파일 Import
"""
import Settings
import Accounts
import Candles
import PrintLog
import Policies
"""
프로그램 시작
"""
PrintLog.pLog("UPbit Trader starts.")
Accounts.printAllAccounts()

"""
가격 예측 / 매매
"""
Policies.trdDayTradeForHunt("KRW-HUNT","HUNT",10000)

