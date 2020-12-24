"""
주식 트레이딩 봇 GUI

[핵심기능]
- 주식 확인 (검색, 리스트) (시간에 따른 현재가)
- 주식 구매, 주식 판매 기능
- 주식 자동화 () 
"""

import win32com.client
import json
 
# 연결 여부 체크
objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
bConnect = objCpCybos.IsConnect
if (bConnect == 0):
    print("PLUS가 정상적으로 연결되지 않음. ")
    exit()
 
# 현재가 객체 구하기
objStockMst = win32com.client.Dispatch("DsCbo1.StockMst")
objStockMst.SetInputValue(0, 'A005930')   #종목 코드 - 삼성전자
objStockMst.BlockRequest()
 
# 현재가 통신 및 통신 에러 처리 
rqStatus = objStockMst.GetDibStatus()
rqRet = objStockMst.GetDibMsg1()
print("통신상태", rqStatus, rqRet)
if rqStatus != 0:
    exit()
 
# 현재가 정보 조회
offer = objStockMst.GetHeaderValue(16)  #매도호가

from slacker import Slacker

with open("data.json", "r") as jData:
    data = json.load(jData)
    slack = Slacker(data["slack"]["botToken"])
    # Send a message to #general channel
    slack.chat.post_message(data["slack"]["chennel"], '삼성전자 현재가: ' + str(offer))