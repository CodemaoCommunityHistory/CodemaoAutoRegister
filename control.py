import random
import requests
import time
import uuid
import json
import logging
from fake_useragent import UserAgent

#logging

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s',
                    level=logging.INFO)

def get_random_phone_code(start):
        return  str(start) + str(random.randint(22119120,98019920))

def send_captcha_code(phone_code,random_ua):
        api_url = 'https://open-service.codemao.cn/captcha/rule/v3'
        device_id = ''.join(str(uuid.uuid4()).split('-'))
        ua = UserAgent().random

        if random_ua :
                api_header = {'Content-Type': 'application/json' , 'User-Agent' : ua}
        else:
                api_header = {'Content-Type': 'application/json'}

        post_data = {}
        post_data.update({"deviceId": device_id, "identity": phone_code, "pid": "65edCTyg", "scene": "",
                          "timestamp": int(time.time())})

        if random_ua:
                logging.info('UserAgent:' + ua + '\n手机号:' + str(phone_code) + '\nDeviceID:' + device_id + '\n')
        else:
                logging.warning('\n[!]推荐开启随机UA!\n手机号:' + str(phone_code) + '\nDeviceID:' + device_id + '\n')

        r = requests.post(api_url, data = json.dumps(post_data) , headers = api_header)

        if json.loads(r.text).get("rule") == "TENCENT" :
                # 触发风控
                logging.error('请求被风控!返回信息:' + r.text)
                return False

        if r.status_code == 200 :
                logging.info('请求成功!返回状态码:' + str(r.status_code) + ',返回信息:' + r.text)
                return True
        else:
                logging.error('请求异常!返回状态码:' + str(r.status_code) + ',返回信息:' + r.text)
                return False

def test_captcha_code(phone_code):
        pass