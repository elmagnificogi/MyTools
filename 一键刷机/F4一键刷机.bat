@echo off
:start
echo 确保你当前J-Link驱动正常，并且连接到了对应的接口上
set "answer=0"
echo 输入1 烧写MCU，2 烧写IMU，3 烧写GPS 回车开始烧写
set /p answer=
if "%answer%"=="1" (echo 开始烧写MCU 
JLink.exe <F407MCU.txt
goto note)
if "%answer%"=="2" (echo 开始烧写IMU
JLink.exe <F407IMU.txt
goto note)
if "%answer%"=="3" (echo 开始烧写GPS
JLink.exe <F103GPS.txt
goto note)
:note
echo 注意查看返回信息中是否有 Failed
echo 如果有重新刷，正确情况下是successful
echo 正确烧写:读完进度条之后有烧写时间提示
echo 如果提示skipped 表示已有固件和当前相同
echo 全部刷完之后断电重启，观察是否指示灯正常
goto start