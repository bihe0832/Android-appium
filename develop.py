
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
    utils.cmd("adb uninstall io.appium.uiautomator2.server.test")
    utils.cmd("adb uninstall io.appium.unlock")
    utils.cmd("adb uninstall io.appium.settings")
def hardytest():
    # port_utils.check_port(4723)
    port_utils.release_port(8200)

if __name__ == '__main__':
    uuid=""
    port=4723
    result = utils.cmd("adb devices")   
    print(result)
    for device in result.split('\n'):
        if device.endswith('\tdevice') == True:
                uuid=device.split('\t')[0]
                break
    print(uuid)

    utils.showDevice(uuid)
    # reinstall()
    desired_caps={}
    desired_caps['platformName']= "Android"
    desired_caps['deviceName']= uuid
    print('appium start run %s at %s' %(uuid,ctime()))
    # hardytest()
    driver=webdriver.Remote('http://127.0.0.1:'+str(port)+'/wd/hub',desired_caps)
    driver.implicitly_wait(appium_const.IMPLICITLY_WAIT_SHORT)
    # utils.wechatlogin(driver,uuid,zixie_const.WECHAT_ID,zixie_const.WECHAT_PASSWORD)
	# utils.qqlogin(driver,uuid,zixie_const.WECHAT_ID,zixie_const.WECHAT_PASSWORD)
    zixie_main.startTest(driver,zixie_const.TEMP_UUID)
