# README

업비트 API GUIDE [https://docs.upbit.com/docs]

- 백그라운드 실행: nohup python3 -u filename.py > output.log &
    - -u 옵션으로 print() output파일에 출력
- 실행 확인: ps ax | grep .py
- 프로세스 종료(PID는 ps ax | grep .py로 확인): kill -9 PID

## .gitignore
- Settings.py

import uuid

import os

import jwt

os.environ['UPBIT_OPEN_API_ACCESS_KEY'] = ''

os.environ['UPBIT_OPEN_API_SECRET_KEY'] = ''

os.environ['UPBIT_OPEN_API_SERVER_URL'] = 'https://api.upbit.com'


access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']

secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']

server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

payload = {
'access_key': access_key,
'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, secret_key)

authorization = 'Bearer {}'.format(jwt_token)

headers = {'Authorization': authorization, }





## 발견된 문제점

1. 일정 비율 도달 시 손절 안됨
2. 같은 자산 보유 중인 경우 조건 충족해도 추가 매수 안하는 알고리즘 작동 안함