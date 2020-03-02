import requests
import sys
import time
import datetime

sys.path.append(r'./const/')
from const import *

def notify(content):
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=" + appium_const.QYWORK
    headers = {"Content-Type": "text/plain"}
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": content,
        }
    }
    r = requests.post(url, headers=headers, json=data)
    print(content)
    print(r.text)
    return r.text


def doActionWithNotify(driver, uuid,module, actionFunc, **kwargs):
    notifyStart(uuid,module)
    try:
        if actionFunc(driver,uuid) == True:
            notifySucc(uuid,module)
            return True
        else:
            notifyFailed(uuid,module)
            return False
    except Exception as e:
        print('repr(e):\t', repr(e))
        notifyFailed(uuid,module)
        return False


def notifyStart(uuid,module):
    notify("设备"+uuid +"上开始执行" + module + "相关测试：" + (datetime.datetime.fromtimestamp(time.time())).strftime("%Y-%m-%d %H:%M:%S"))

def notifySucc(uuid,module):
    notify("设备"+uuid +"上执行的" + module + "相关测试已完成：测试成功~")

def notifyFailed(uuid,module):
    notify("<font color=\"info\">设备"+uuid +"上执行的" + module + "相关测试已完成：测试失败~</font>")