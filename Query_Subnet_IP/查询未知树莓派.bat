COLOR 0A
CLS
@ECHO Off
Title 查询局域网内在线IP
:send
@ECHO off&setlocal enabledelayedexpansion
ECHO 正在获取本机的IP地址，请稍等... 
for /f "tokens=4 skip=2 delims=: " %%i in ('nbtstat -n') do ( 
set "IP=%%i" 
set IP=!IP:~1,-1!  
ECHO 本机IP为：!IP! 
goto :next 
)
:next 
ECHO.
ECHO 正在获取本网段内的其它曾加入路由表的IP(并不一定表示在线,只是表示连接过)，请稍等... 
ECHO 清空当前路由表连接记录,需要使用管理员权限运行本bat
arp -d
for /L %%j IN (101,1,233) DO ping -w 2 -n 1 192.168.1.%%j
for /f "skip=3 tokens=1,* delims= " %%i in ('arp -a') do ECHO IP： %%i 处于路由表中
ECHO.
ECHO 查询完毕，按任意键退出...
pause>nul