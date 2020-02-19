import requests
import sys
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


