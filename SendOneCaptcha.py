# @author: Wangs_official
# @LICENSE: MIT
# Please read README.md when you start to use

import logging
import control as c
import argparse

parser = argparse.ArgumentParser(description="CodemaoAutoRegister-SOC")
parser.add_argument("-p", "--phone", help="11 Phone Code" , type=int)
args = parser.parse_args()

c.send_captcha_code(args.phone,True)