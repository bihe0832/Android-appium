
from appium import webdriver
from  time import  ctime
from selenium.webdriver.support.ui import WebDriverWait
import sys
import multiprocessing
sys.path.append(r'./zixie/')
sys.path.append(r'./common/')
sys.path.append(r'./appium/')
sys.path.append(r'./const/')
from const import *
import utils
import zixie_main
import port_utils

def reinstall():
    utils.cmd("adb uninstall io.appium.uiautomator2.server")
    utils.cmd("adb  uninstall io.appium.uiautomator2.server.test")

def hardytest():
    # port_utils.check_port(4723)
    port_utils.release_port(8200)

if __name__ == '__main__':
    # hardytest()

    reinstall()
    desired_caps={}
    desired_caps['platformName']= "Android"
    desired_caps['deviceName']= zixie_const.TEMP_UUID
    print('appium start run %s at %s' %(zixie_const.TEMP_UUID,ctime()))
    driver=webdriver.Remote('http://localhost:'+str(zixie_const.TEMP_PORT)+'/wd/hub',desired_caps)
    driver.implicitly_wait(appium_const.IMPLICITLY_WAIT_SHORT)
    zixie_main.startTest(driver,zixie_const.TEMP_UUID)
