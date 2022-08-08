import Candles
import PrintLog
import Accounts

"""
Bullish(강세)(양봉) 
Bearish(약세)(음봉)
"""

def trdDayTradeForHunt():
    candles = Candles.getDayCandles("KRW-HUNT","3")
    if candles[0]['trade_price'] < candles[0]['opening_price']:
        PrintLog.pLog("Today_Bearish Candle.")
        return False
    else:
        for candle in candles:
            if candle['trade_price'] < candle['opening_price']:
                PrintLog.pLog("Bearish Candle Exists.")
                return False
        PrintLog.pLog("Check Coin Exists in Account")
        balance = Accounts.getBalanceFromCodeP("KRW-HUNT")
        if balance == None:
            PrintLog.pLog("Buy KRW-HUNT")

        else:
            PrintLog.pLog("We Have KRW-HUNT Now.")

trdDayTradeForHunt()