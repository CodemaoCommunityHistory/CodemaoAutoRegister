# @author: Wangs_official
# @LICENSE: MIT
# Please read README.md when you start to use

import logging
import control as c
import argparse
import time as t
import uuid as u
import _thread
from fake_useragent import UserAgent

run_t = 0

ua = UserAgent().random

parser = argparse.ArgumentParser(description="CodemaoAutoRegister-TCC")
parser.add_argument("-p", "--phone", help="11 Phone Code" , type=int)
parser.add_argument("-w", "--wait_time", help="The number of seconds between each code transmission" , type=int , default=10)

args = parser.parse_args()

start_time = t.time()
duration = 10 * 60
password = ''.join(str(u.uuid4()).split('-'))[20:]

logging.info(f'开始穷举,密码:{password}')

while 1:

    a = _thread.start_new_thread(c.test_captcha_code , (args.phone , password , ua))
    b = _thread.start_new_thread(c.test_captcha_code , (args.phone , password , ua))
    c1 = _thread.start_new_thread(c.test_captcha_code , (args.phone , password , ua))
    d =_thread.start_new_thread(c.test_captcha_code , (args.phone , password , ua))
    e =_thread.start_new_thread(c.test_captcha_code , (args.phone , password , ua))
    f =_thread.start_new_thread(c.test_captcha_code , (args.phone , password , ua))
    g =_thread.start_new_thread(c.test_captcha_code , (args.phone , password , ua))
    h =_thread.start_new_thread(c.test_captcha_code , (args.phone , password , ua))

    if not a:
        exit()
    else:
        run_t = run_t +1
        logging.info(f'已运行:{run_t}次')
        elapsed_time = t.time() - start_time
        if elapsed_time >= duration:
            logging.error('穷举失败(超时),请重新执行程序!')
            exit()

    if not b:
        exit()
    else:
        run_t = run_t + 1
        logging.info(f'已运行:{run_t}次')
        elapsed_time = t.time() - start_time
        if elapsed_time >= duration:
            logging.error('穷举失败(超时),请重新执行程序!')
            exit()

    if not c1:
        exit()
    else:
        run_t = run_t + 1
        logging.info(f'已运行:{run_t}次')
        elapsed_time = t.time() - start_time
        if elapsed_time >= duration:
            logging.error('穷举失败(超时),请重新执行程序!')
            exit()

    if not d:
        exit()
    else:
        run_t = run_t + 1
        logging.info(f'已运行:{run_t}次')
        elapsed_time = t.time() - start_time
        if elapsed_time >= duration:
            logging.error('穷举失败(超时),请重新执行程序!')
            exit()

    if not e:
        exit()
    else:
        run_t = run_t + 1
        logging.info(f'已运行:{run_t}次')
        elapsed_time = t.time() - start_time
        if elapsed_time >= duration:
            logging.error('穷举失败(超时),请重新执行程序!')
            exit()

    if not f:
        exit()
    else:
        run_t = run_t + 1
        logging.info(f'已运行:{run_t}次')
        elapsed_time = t.time() - start_time
        if elapsed_time >= duration:
            logging.error('穷举失败(超时),请重新执行程序!')
            exit()
            
    if not g:
        exit()
    else:
        run_t = run_t + 1
        logging.info(f'已运行:{run_t}次')
        elapsed_time = t.time() - start_time
        if elapsed_time >= duration:
            logging.error('穷举失败(超时),请重新执行程序!')
            exit()

    if not h:
        exit()
    else:
        run_t = run_t + 1
        logging.info(f'已运行:{run_t}次')
        elapsed_time = t.time() - start_time
        if elapsed_time >= duration:
            logging.error('穷举失败(超时),请重新执行程序!')
            exit()

    t.sleep(args.wait_time)