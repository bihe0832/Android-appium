
from appium import webdriver
from  time import  ctime
from selenium.webdriver.support.ui import WebDriverWait
import sys
from time import sleep
import multiprocessing
sys.path.append(r'./common/')
sys.path.append(r'./const/')
from const import *
import utils
import port_utils

#appium进程组
appium_process=[]

def appium_start(host,port):
    if port_utils.check_port(port) == True:
        port_utils.release_port(port)

    cmd = '/usr/local/bin/appium -a ' + host + ' -p ' + str(port) + ' -g ./log/appium_server_'+str(port)+'.log'
    print('%s at %s' %(cmd, ctime()))
    utils.cmd(cmd)

def appium_start_sync(devices_list, host,firstPort):
    #加载appium进程
    for i in range(len(devices_list)):
        port = firstPort + 2 * i
        appium=multiprocessing.Process(target=appium_start,args=(host,port))
        appium_process.append(appium)
    #并发启动appium服务
    for appium in appium_process:
        appium.start()
    for appium in appium_process:
        appium.join()

if __name__ == '__main__':
    # host='127.0.0.1'
    # firstPort=4725

    # 可用设备列表
    devices_list=[]
    result = utils.cmd("adb devices")   
    print(result)
    for device in result.split('\n'):
        if device.endswith('\tdevice') == True:
            devices_list.append(device.split('\t')[0])
    print(devices_list)       
    appium_start_sync(devices_list,appium_const.HOST,appium_const.FIRST_PORT)

    

    
    
