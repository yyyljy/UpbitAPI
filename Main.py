from ssl import ALERT_DESCRIPTION_ACCESS_DENIED
from tkinter.filedialog import SaveFileDialog
import requests
from urllib.parse import urlencode, unquote
import json
import Settings
import Accounts
import Candles

# krwBalance = Accounts.getBalanceFromCode('KRW')
# print(krwBalance)

# huntCandle = Candles.getDayCandle("KRW-HUNT")
# print(huntCandle)

# huntCandle2 = Candles.getDayCandles("KRW-HUNT", "2")
# print(huntCandle2)

huntCandle3 = Candles.getDayCandlesTo("KRW-HUNT", "2022-08-02 24:00:00", "2")
print(huntCandle3)
