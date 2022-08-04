import Settings

"""
시세 종목 조회
"""
# 마켓 코드 조회
def getMarketsURL(unit):
    return Settings.server_url + "/v1/market/all"

"""
시세 캔들 조회
"""
# 분(Minute) 캔들
def getMinutesURL(unit):
    return Settings.server_url + "/v1/candles/minutes/" + unit

# 일(Day) 캔들
def getDaysURL():
    return Settings.server_url + "/v1/candles/days"

# 주(Week) 캔들
def getWeeksURL():
    return Settings.server_url + "/v1/candles/weeks"

# 월(Month) 캔들
def getMonthsURL():
    return Settings.server_url + "/v1/candles/months"


"""
시세 체결 조회
"""
# 최근 체결 내역
def getMonthsURL():
    return Settings.server_url + "/v1/trades/ticks"
