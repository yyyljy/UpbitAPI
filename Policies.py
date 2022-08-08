import re
import Candles
import PrintLog
import Accounts
import Trades

"""
Bullish(강세)(양봉) 
Bearish(약세)(음봉)
"""

def trdDayTradeForHunt(market, code, orderKRW):
    candles = Candles.getDayCandles(market,"3")
    price = candles[0]['trade_price']
    volume = round(orderKRW / candles[0]['trade_price'], 8)
    if candles[0]['trade_price'] < candles[0]['opening_price']:
        PrintLog.pLog("Today_Bearish Candle.")
        return False
    else:
        for candle in candles:
            if candle['trade_price'] < candle['opening_price']:
                PrintLog.pLog("Bearish Candle Exists.")
                return False
        PrintLog.pLog("Check Coin Exists in Account")
        balance = Accounts.getBalanceFromCodeP(code)
        balance = None
        if balance == None:
            PrintLog.pLog("Let's Buy "+ market)
            marketInfo = Trades.getOrderChance(market)
            if marketInfo['market']['state'] == 'active':
                pass
            else:
                PrintLog.pLog("ERROR : " + market + "STATE IS NOT ACTIVE")
                return False
            tradesLeft = Trades.getOrdersList()
            for trade in tradesLeft:
                if trade['market'] == market and trade['side'] == 'bid':
                    PrintLog.pLog("Cancel Bid Offer Left")
                    result = Trades.deleteOrder(trade['uuid'])
                    if result == False:
                        PrintLog.pLog("ERROR : Cancel Bid-Offer-Left Failed")
                        return False
                    else:
                        PrintLog.pLog("Cancel-Bid-Offer-Left Success")
            # Trades.orderMarketPrice(market,'bid',volume,price+1)
            PrintLog.pLog("Order Market : " + market + " Volume : " + str(volume) + " Price : " + str(int(price)+1))
        else:
            PrintLog.pLog("We Have " + market + " Now.")
            return False