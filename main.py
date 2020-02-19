
from appium import webdriver
from time import *
from selenium.webdriver.support.ui import WebDriverWait
import sys
from time import sleep
import multiprocessing
sys.path.append(r'./common/')
sys.path.append(r'./zixie/')
sys.path.append(r'./const/')
sys.path.append(r'./appium/')
from const import *
import utils
import zixie_main

def appium_desired(udid,port):
    f = open('./log/appium_client_'+udid+'_'+str(port)+'.log', 'w')
    # sys.stdout = f
    desired_caps={}
    desired_caps['platformName']= "Android"
    desired_caps['deviceName']= udid
    print('%s start run on appium port:%s at %s' %(udid,port,ctime()))
    driver=webdriver.Remote('http://'+appium_const.HOST+':'+str(port)+'/wd/hub',desired_caps)
    sleep(appium_const.IMPLICITLY_WAIT_SHORT)
    driver.implicitly_wait(appium_const.IMPLICITLY_WAIT_SHORT)
    zixie_main.startTest(driver,udid)
 	driver.quit()
    f.close()
# 可用设备列表
devices_list=[]
#appium进程组
appium_process=[]
#定义desired进程组
desired_process = []

def appium_desired_sync(firstPort):
   #加载desied进程
    for i in range(len(devices_list)):
        port = firstPort + 2 * i
        desired= multiprocessing.Process(target=appium_desired,args=(devices_list[i],port))
        desired_process.append(desired)

    # 启动多设备执行测试
    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()

if __name__ == '__main__':
    result = utils.cmd("adb devices")   
    print(result)
    for device in result.split('\n'):
        if device.endswith('\tdevice') == True:
            devices_list.append(device.split('\t')[0])
    print(devices_list)       
    appium_desired_sync(appium_const.FIRST_PORT)
    

    
    
