from appium import webdriver
from  time import  ctime
from selenium.webdriver.support.ui import WebDriverWait
import multiprocessing
import sys
sys.path.append(r'./../common/')
sys.path.append(r'./../const/')
from const import *
import utils
import time

def startTest(driver,udid):
    utils.showDevice(udid)
    utils.wechatlogin(driver,udid,zixie_const.WECHAT_ID,zixie_const.WECHAT_PASSWORD)


