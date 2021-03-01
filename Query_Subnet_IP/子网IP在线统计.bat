:::::::查看所有子网IP.bat:::::::
@echo off
title 查看所有子网IP
 
set /a Online=0
set /a Offline=0
set /a Total=256
set ExportFile=子网IP在线统计.txt
:: 初始化在线IP与不在线IP的个数为零，共扫描256个IP，结果输出的文件名
 
set StartTime=%time%
:: 记录程序的开始时间
 
for /f "delims=: tokens=2" %%i in ('ipconfig /all ^| find /i "IPv4"') do set IP=%%i
:: 获得本机IP [注1]
 
if "%IP%"=="" echo 未连接到网络 & pause & goto :EOF
if "%IP%"==" 0.0.0.0" echo 未连接到网络 & pause & goto :EOF
:: 当IP为空或 0.0.0.0 时，提示未连接并退出该程序
 
for /f "delims=. tokens=1,2,3,4" %%i in ("%IP%") do (
  set /a IP1=%%i
  set /a IP2=%%j
  set /a IP3=%%k
  set /a IP4=%%l
)
:: 这里其实可以修改查询的IP子网 无视循环直接修改
:: 以句点为分隔符，分别将IP的四个十进制数赋给四个变量

echo %IP1%
echo %IP2%
echo %IP3%
echo %IP4%
 
set /a IP4=0
echo 在线的IP：>%ExportFile%
:: 初始化IP的第四个数值为0，并创建结果输出文件,需要查询的起点在这里
 
:RETRY
ping %IP1%.%IP2%.%IP3%.%IP4% -n 1 -w 200 -l 16>nul && set /a Online+=1 && echo %IP1%.%IP2%.%IP3%.%IP4%>>%ExportFile% || set /a Offline+=1
:: ping 目标IP [注2]
 

set /a Scanned=%Online%+%Offline%
set /a Progress=(%Online%+%Offline%)*100/%Total%
echo 正在扫描：%Scanned%/%Total% 扫描进度：%Progress%%%
 
set /a IP4+=1
:: 每次查询的步长在这里
if %IP4% lss %Total% goto :RETRY
:: 当IP的第四个数值小于总数时，跳转回 :RETRY 处，重复执行直到全部 ping 完为止
 
echo.
echo.
 
set EndTime=%time%
:: 记录程序的结束时间
 
set /a Seconds = %EndTime:~6,2% - %StartTime:~6,2%
set /a Minutes = %EndTime:~3,2% - %StartTime:~3,2%
if %Seconds% lss 0 set /a Seconds += 60 & set /a Minutes -= 1
if %Minutes% lss 0 set /a Minutes += 60
:: 计算时间差
 
set /a Percent=%Online%*100/(%Online%+%Offline%)
:: 计算在线百分比
 
echo 在线IP个数:  %Online%
echo 不在线IP个数: %Offline%
echo 在线百分比:  %Percent%%%
echo 统计耗时:   %Minutes%分%Seconds%秒
echo 统计日期:   %date% %time:~0,-3%
echo.>>%ExportFile%
echo 在线IP个数:  %Online%>>%ExportFile%
echo 不在线IP个数: %Offline%>>%ExportFile%
echo 在线百分比:  %Percent%%%>>%ExportFile%
echo 统计耗时:   %Minutes%分%Seconds%秒>>%ExportFile%
echo 统计日期:   %date% %time:~0,-3%>>%ExportFile%
echo 记录已保存到文件"%ExportFile%"中
::显示结果并将结果保存到文件中
pause