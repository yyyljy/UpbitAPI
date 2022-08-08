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

"""
프로그램 시작
"""
PrintLog.pLog("UPbit Trader starts.")
Accounts.printAllAccounts()

"""
가격 예측
"""
# huntCandle3 = Candles.getDayCandlesTo("KRW-HUNT", "2022-08-02 24:00:00", "2")
# print(huntCandle3)