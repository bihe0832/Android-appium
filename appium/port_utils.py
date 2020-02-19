import socket
import os
def check_port(port):
   #查找对应端口的pid
    cmd_find='lsof -i tcp:%s' %port
    print(cmd_find)

    #返回命令执行后的结果
    result = os.popen(cmd_find).read()
    print(result)
    for portInfo in result.split('\n'):
        if str(port) in portInfo:
            print('check_port port %s already be in use!' % port)
            return True
    
    print('check_port port %s is available !' %port)
    return False

def release_port(port):
    #查找对应端口的pid
    cmd_find='lsof -i tcp:%s' %port
    print(cmd_find)

    #返回命令执行后的结果
    result = os.popen(cmd_find).read()
    print(result)
    for portInfo in result.split('\n'):
        if str(port) in portInfo:
            print(portInfo.split(' '))
            print((' '.join(portInfo.split())).split(' '))
            # 关闭被占用端口的pid
            cmd_kill='kill ' + (' '.join(portInfo.split())).split(' ')[1]
            print(cmd_kill)
            os.popen(cmd_kill)
            print('release_port port %s already be in use ,but now is available!' % port)
            return 
    print('release_port port %s is available !' %port)

if __name__ == '__main__':
    host='127.0.0.1'
    port=4723
    # check_port(host,port)