@echo off
:start
echo ȷ���㵱ǰJ-Link�����������������ӵ��˶�Ӧ�Ľӿ���
set "answer=0"
echo ����1 ��дMCU��2 ��дIMU��3 ��дGPS �س���ʼ��д
set /p answer=
if "%answer%"=="1" (echo ��ʼ��дMCU 
JLink.exe <F407MCU.txt
goto note)
if "%answer%"=="2" (echo ��ʼ��дIMU
JLink.exe <F407IMU.txt
goto note)
if "%answer%"=="3" (echo ��ʼ��дGPS
JLink.exe <F103GPS.txt
goto note)
:note
echo ע��鿴������Ϣ���Ƿ��� Failed
echo ���������ˢ����ȷ�������successful
echo ��ȷ��д:���������֮������дʱ����ʾ
echo �����ʾskipped ��ʾ���й̼��͵�ǰ��ͬ
echo ȫ��ˢ��֮��ϵ��������۲��Ƿ�ָʾ������
goto start