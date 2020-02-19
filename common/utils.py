import time
import subprocess
import os
import datetime
from selenium.webdriver.support.ui import WebDriverWait
import sys
from time import sleep
sys.path.append(r'./const/')
from const import *

def cmd(command):
    subp = subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    if subp.returncode == 0:
        return str(subp.stdout)
    else:
        return "Failed" 

def screenshot(driver,content):
    log(content)
    file_name = './screenshot/appium_'+content[0:content.find('.')]+'_' + str(int(time.time()))+'.png'
    log(file_name)
    driver.save_screenshot(file_name)
    driver.implicitly_wait(appium_const.IMPLICITLY_WAIT_SHORT)

def log(msg):
    timeNow = time.time()
    print( (datetime.datetime.fromtimestamp(timeNow)).strftime("%Y-%m-%d %H:%M:%S/") + str(int(timeNow)) + " "+ msg +"\n")

def showDevice(uuid):
    print("************** device info of :"+uuid+" **************")
    print("brand:" + cmd("adb -s " +uuid+ " shell getprop ro.product.brand"))
    print("model:" + cmd("adb -s " +uuid+ " shell getprop ro.product.model"))
    print("manufacturer:" + cmd("adb -s " +uuid+ " shell getprop ro.product.manufacturer"))
    print("version.release:" + cmd("adb -s " +uuid+ " shell getprop ro.build.version.release"))
    print("version.sdk:" + cmd("adb -s " +uuid+ " shell getprop ro.build.version.sdk"))
    cmd("adb -s " +uuid+ " shell wm size")
    print("************** device info of :"+uuid+" **************")

def wechatlogin(driver,uuid, username,password):
    cmd("adb -s " +uuid+ " shell pm clear com.tencent.mm")

    log("start wechat app")
    cmd("adb -s " +uuid+ " shell am start com.tencent.mm/com.tencent.mm.ui.LauncherUI")
    try:
        driver.wait_activity(".plugin.account.ui.WelcomeActivity", 10) 
    except Exception as e:
        log('repr ui.WelcomeActivity:\t'+ repr(e))
        return False

    try:
        WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//android.widget.Button[contains(@text, "登录")]').is_displayed())
    except Exception as e:
        log('repr login:\t'+ repr(e))
        screenshot(driver, os.path.basename(__file__))
        return False
    log("start login")
    driver.find_element_by_xpath('//android.widget.Button[contains(@text, "登录")]').click()
    
    try:
        driver.wait_activity(".plugin.account.ui.MobileInputUI", 10) 
    except Exception as e:
        log('repr ui.MobileInputUI:\t'+ repr(e))
        return False

    log("change wechat app login to qq")
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[1]").click()
    try:
        driver.wait_activity(".plugin.account.ui.LoginUI", 10) 
    except Exception as e:
        log('repr ui.LoginUI:\t'+ repr(e))
        return False
    driver.implicitly_wait(appium_const.IMPLICITLY_WAIT_SHORT)

    id = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText")
    id.send_keys(username)
    pswd = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText")
    pswd.send_keys(password)
    
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]").click()
    driver.find_element_by_xpath('//android.widget.Button[contains(@text, "我知道了")]').click()

    try:
        driver.wait_activity(".ui.LauncherUI", 10) 
    except Exception as e:
        log('repr .ui.LauncherUI:\t' + repr(e))
        screenshot(driver, os.path.basename(__file__))
        return False

    try:
        WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="当前所在页面,与的聊天"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]').is_displayed())
    except Exception as e:
        log('repr main:\t'+ repr(e))
        screenshot(driver, os.path.basename(__file__))
        return False
    else:
        log('wechat login succ')
        return True


