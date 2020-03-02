## Android-appium

### 简介

基于Appium的Android自动化测试框架。在实际开发中 ，我们可能会同时在多台设备上运行测试用例，为了提高效率，个人专门开发了这套多进程并发运行测试用例的demo。

### 环境搭建

环境搭建可以参考：

- appium爬坑之iMac上appium环境搭建及使用真机测试Android项目简介：

    [https://blog.bihe0832.com/appium-desktop-imac.html](https://blog.bihe0832.com/appium-desktop-imac.html)
    
- appium爬坑之iMac上基于appium多设备并发测试

    [https://blog.bihe0832.com/appium-command.html](https://blog.bihe0832.com/appium-command.html)

### 框架介绍
    
    ├── appium  : appium 并发启动server
    │   ├── appium_server.py
    │   └── port_utils.py
    ├── common  : 基础工具类
    │   ├── qywork.py
    │   └── utils.py
    ├── const   ：常量定义
    │   └── const.py
    ├── develop.py  ：指定设备运行测试用例
    ├── main.py ：并发批量设备运行测试用例
    └── zixie   ： demo测试用例
        └── zixie_main.py

** 备注：框架提供的QQ和TIM登录会清空当前手机上对应应用的所有数据**

### 实例运行

#### 启动服务器

    ➜  Android-appium git:(master) ✗ find ./ -name "__pycache__" | xargs -I {} rm -fr {} && find ./log | xargs -I {} rm -fr {} &&  find ./screenshot | xargs -I {} rm -fr {} && python3.7 appium/appium_server.py
    
    List of devices attached
    4fb845e3	device
    
    
    ['4fb845e3']
    lsof -i tcp:4725
    COMMAND   PID  USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
    node    75277 zixie   22u  IPv4 0x28a52c751176dd2f      0t0  TCP localhost:4725 (LISTEN)
    
    check_port port 4725 already be in use!
    lsof -i tcp:4725
    COMMAND   PID  USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
    node    75277 zixie   22u  IPv4 0x28a52c751176dd2f      0t0  TCP localhost:4725 (LISTEN)
    
    ['node', '', '', '', '75277', 'zixie', '', '', '22u', '', 'IPv4', '0x28a52c751176dd2f', '', '', '', '', '', '0t0', '', 'TCP', 'localhost:4725', '(LISTEN)']
    ['node', '75277', 'zixie', '22u', 'IPv4', '0x28a52c751176dd2f', '0t0', 'TCP', 'localhost:4725', '(LISTEN)']
    kill 75277
    release_port port 4725 already be in use ,but now is available!
    /usr/local/bin/appium -a 127.0.0.1 -p 4725 -g ./log/4725.log at Wed Feb 19 13:54:21 2020

#### 运行测试用例

    ➜  Android-appium git:(master) ✗ python3.7 main.py
    List of devices attached
    4fb845e3	device
    
    
    ['4fb845e3']
    appium port:4725 start run 4fb845e3 at Wed Feb 19 13:56:37 2020
    ************** device info of :4fb845e3 **************
    brand:blackshark
    
    model:SKW-A0
    
    manufacturer:blackshark
    
    version.release:9
    
    version.sdk:28
    
    ************** device info of :4fb845e3 **************
    2020-02-19 13:56:43/1582091803 start wechat app

#### 指定设备调试


    ➜  Android-appium git:(master) ✗ python3.7 develop.py
    appium start run 4fb845e3 at Wed Feb 19 13:58:17 2020
    ************** device info of :4fb845e3 **************
    brand:blackshark
    
    model:SKW-A0
    
    manufacturer:blackshark
    
    version.release:9
    
    version.sdk:28
    
    ************** device info of :4fb845e3 **************
    2020-02-19 13:58:22/1582091902 start wechat app


### 相关文章

- appium爬坑之iMac上appium环境搭建及使用真机测试Android项目简介：

    [https://blog.bihe0832.com/appium-desktop-imac.html](https://blog.bihe0832.com/appium-desktop-imac.html)
    
- appium爬坑之iMac上基于appium多设备并发测试

    [https://blog.bihe0832.com/appium-command.html](https://blog.bihe0832.com/appium-command.html)

- appium 爬坑之基于 Chromedriver 测试 Android webview 
	
	[https://blog.bihe0832.com/appium-android-webview.html](https://blog.bihe0832.com/appium-android-webview.html)

