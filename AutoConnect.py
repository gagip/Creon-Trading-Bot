"""Creon 자동 로그인 모듈"""
from pywinauto import application
import time
import os
import json


class AutoConnect():
    """Creon 자동 로그인 클래스"""
    def connect(self):
        """자동 로그인"""
        os.system('taskkill /IM coStarter* /F /T')
        os.system('taskkill /IM CpStart* /F /T')
        os.system('wmic process where "name like \'%coStarter%\'" call terminate')
        os.system('wmic process where "name like \'%CpStart%\'" call terminate')
        time.sleep(5)        

        # 개인 데이터 불러오기
        with open("data.json", "r") as jsonFile:
            data = json.load(jsonFile)

        # 자동 로그인
        app = application.Application()
        app.start(data["creon"])
        time.sleep(60)