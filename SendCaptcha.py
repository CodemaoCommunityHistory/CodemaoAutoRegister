# @author: Wangs_official
# @LICENSE: MIT

"""
SendCaptcha.py

We want to be consistent, so we removed this file from CodemaoAutoRegister.
If you want to use it, please download this file, then open the command line and install the requests library, like this

pip3 install requests

Then, please enter this string of commands to run it

python3 SendCaptcha.py -w <间隔时间(单位秒)> -ru <随机UA(True/False)>

Origin repo : https://github.com/Wangs-official/CodemaoAutoRegister

"""

from fake_useragent import UserAgent
import logging
import argparse
import time as t
import uuid
import requests
import random
import json

# def

def get_random_phone_code(start):
    return str(start) + str(random.randint(22119120, 98019920))


def send_captcha_code(phone_code, random_ua):
    api_url = 'https://open-service.codemao.cn/captcha/rule/v3'
    device_id = ''.join(str(uuid.uuid4()).split('-'))
    ua = UserAgent().random

    if random_ua:
        api_header = {'Content-Type': 'application/json', 'User-Agent': ua}
    else:
        api_header = {'Content-Type': 'application/json'}

    post_data = {}
    post_data.update({"deviceId": device_id, "identity": phone_code, "pid": "65edCTyg", "scene": "",
                      "timestamp": int(t.time())})

    if random_ua:
        logging.info('UserAgent:' + ua + '\n手机号:' + str(phone_code) + '\nDeviceID:' + device_id + '\n')
    else:
        logging.warning('\n[!]推荐开启随机UA!\n手机号:' + str(phone_code) + '\nDeviceID:' + device_id + '\n')

    r = requests.post(api_url, data=json.dumps(post_data), headers=api_header)

    if json.loads(r.text).get("rule") == "TENCENT":
        # 触发风控
        logging.error('请求被风控!返回信息:' + r.text)
        return False

    if r.status_code == 200:
        logging.info('请求成功!返回状态码:' + str(r.status_code) + ',返回信息:' + r.text)
        return True
    else:
        logging.error('请求异常!返回状态码:' + str(r.status_code) + ',返回信息:' + r.text)
        return False

# argparse

parser = argparse.ArgumentParser(description="CodemaoAutoRegister-SC")
parser.add_argument("-w", "--wait_time", help="The number of seconds between each code transmission" , type=int , default=10)
parser.add_argument("-ru", "--random_ua", help="Random UA" , type=bool , default=True)
args = parser.parse_args()

# Start

run_f = 0

while 1:

    req = send_captcha_code(get_random_phone_code(183),args.random_ua)
    if not req :
        exit()
    else:
        run_f = run_f + 1
        logging.info('运行次数:' + str(run_f)+ '\n')
    t.sleep(args.wait_time)
    req =  send_captcha_code(get_random_phone_code(139),args.random_ua)
    if not req :
        exit()
    else:
        run_f = run_f + 1
        logging.info('运行次数:' + str(run_f)+ '\n')
    t.sleep(args.wait_time)
    req = send_captcha_code(get_random_phone_code(153),args.random_ua)
    if not req :
        exit()
    else:
        run_f = run_f + 1
        logging.info('运行次数:' + str(run_f)+ '\n')
    t.sleep(args.wait_time)
    req = send_captcha_code(get_random_phone_code(188),args.random_ua)
    if not req :
        exit()
    else:
        run_f = run_f + 1
        logging.info('运行次数:' + str(run_f) + '\n')
    t.sleep(args.wait_time)

