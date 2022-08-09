import time
import schedule

"""
구현 파일 Import
"""
import Accounts
import PrintLog
import Policies
"""
프로그램 시작
"""
PrintLog.pLog("UPbit Trader starts.")
Accounts.printAllAccounts()

"""
매매 - 매수(매일 오전 8시 50분)
"""
schedule.every().day.at("08:50").do(Policies.trdDayTradeForHunt,"KRW-HUNT","HUNT",10000)

"""
매매 - 매도(매 분 가격 확인)
"""
schedule.every(1).minutes.do(Policies.checkPriceAndTrade,"KRW-HUNT", "HUNT", 0.1, 0.05)

while True:
    schedule.run_pending()
    time.sleep(1)