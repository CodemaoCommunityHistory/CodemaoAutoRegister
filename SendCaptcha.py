# @author: Wangs_official
# @LICENSE: MIT
# Please read README.md when you start to use
import logging

import control as c
import argparse
import time as t

# argparse

parser = argparse.ArgumentParser(description="CodemaoAutoRegister-SC")
parser.add_argument("-w", "--wait_time", help="The number of seconds between each code transmission" , type=int , default=10)
parser.add_argument("-ru", "--random_ua", help="Random UA" , type=bool , default=True)
args = parser.parse_args()

# Start

run_f = 0

while 1:

    req =  c.send_captcha_code(c.get_random_phone_code(183),args.random_ua)
    if not req :
        exit()
    else:
        run_f = run_f + 1
        logging.info('运行次数:' + str(run_f)+ '\n')
    t.sleep(args.wait_time)
    req =  c.send_captcha_code(c.get_random_phone_code(139),args.random_ua)
    if not req :
        exit()
    else:
        run_f = run_f + 1
        logging.info('运行次数:' + str(run_f)+ '\n')
    t.sleep(args.wait_time)
    req =  c.send_captcha_code(c.get_random_phone_code(153),args.random_ua)
    if not req :
        exit()
    else:
        run_f = run_f + 1
        logging.info('运行次数:' + str(run_f)+ '\n')
    t.sleep(args.wait_time)
    req =  c.send_captcha_code(c.get_random_phone_code(188),args.random_ua)
    if not req :
        exit()
    else:
        run_f = run_f + 1
        logging.info('运行次数:' + str(run_f) + '\n')
    t.sleep(args.wait_time)

logging.info('运行结束!')

