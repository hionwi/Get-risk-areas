# coding=utf-8
import win32api
import hashlib
import logging
import time
import requests

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

data = None


def get_data():
    global data
    url = "http://103.66.32.242:8005/zwfwMovePortal/interface/interfaceJson"

    timestamp = str(int(time.time()))
    nonceHeader = "123456789abcdefg"
    signatureHeaderStr = timestamp + \
        "23y0ufFl5YxIyGrI8hWRUZmKkvtSjLQA" + nonceHeader + timestamp
    signatureHeader = hashlib.sha256(
        signatureHeaderStr.encode(encoding="UTF-8")).hexdigest()

    payload = {
        "appId": "NcApplication",
        "paasHeader": "zdww",
        "timestampHeader": timestamp,
        "nonceHeader": nonceHeader,
        "signatureHeader": signatureHeader.upper(),
        "key": "3C502C97ABDA40D0A60FBEE50FAAD1DA"
    }

    signatureStr = timestamp + "fTN2pfuisxTavbTuYVSsNJHetwq5bJvCQkjjtiLM2dCratiA" + timestamp
    signature = hashlib.sha256(
        signatureStr.encode(encoding="UTF-8")).hexdigest()
    headers = {
        'x-wif-nonce': 'QkjjtiLM2dCratiA',
        'x-wif-paasid': 'smt-application',
        'x-wif-signature': signature.upper(),
        'x-wif-timestamp': timestamp,
    }

    response = requests.post(url, headers=headers, json=payload)

    response_json = response.json()
    return response_json


response_json = get_data()
while True:
    search_city_name = input("输入城市名字\n")
    for high in response_json['data']['highlist']:
        if search_city_name in high['city'] or search_city_name in high['area_name']:
            print("高风险地区\n")
    for middle in response_json['data']['middlelist']:
        if search_city_name in middle['city'] or search_city_name in middle['area_name']:
            print("中风险地区\n")
