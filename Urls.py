import Settings

"""
자산
"""
# 전체 계좌 조회
def getAccountsURL():
    return Settings.server_url + "/v1/accounts"

"""
주문
"""
# 주문 가능 정보
def getOrdersChanceURL():
    # requests.get(server_url + '/v1/orders/chance', params=params, headers=headers)
    return Settings.server_url + "/v1/orders/chance"

# 개별 주문 조회
def getOrderURL():
    # requests.get(server_url + '/v1/order', params=params, headers=headers)
    return Settings.server_url + "/v1/order"

# 주문 리스트 조회
def getOrdersURL():
    # requests.get(server_url + '/v1/orders', params=params, headers=headers)
    return Settings.server_url + "/v1/orders"

# 주문 취소 접수
def deleteOrderURL():
    # requests.delete(server_url + '/v1/order', params=params, headers=headers)
    return Settings.server_url + "/v1/order"

# 주문하기
def PostOrdersURL():
    # requests.post(server_url + '/v1/orders', json=data, headers=headers)
    return Settings.server_url + "/v1/orders"

"""
시세 종목 조회
"""
# 마켓 코드 조회
def getMarketsURL():
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

"""
시세 Ticker 조회
"""
# 현재가 정보
def getTickerURL():
    return Settings.server_url + "/v1/ticker"