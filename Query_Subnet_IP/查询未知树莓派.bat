COLOR 0A
CLS
@ECHO Off
Title ��ѯ������������IP
:send
@ECHO off&setlocal enabledelayedexpansion
ECHO ���ڻ�ȡ������IP��ַ�����Ե�... 
for /f "tokens=4 skip=2 delims=: " %%i in ('nbtstat -n') do ( 
set "IP=%%i" 
set IP=!IP:~1,-1!  
ECHO ����IPΪ��!IP! 
goto :next 
)
:next 
ECHO.
ECHO ���ڻ�ȡ�������ڵ�����������·�ɱ��IP(����һ����ʾ����,ֻ�Ǳ�ʾ���ӹ�)�����Ե�... 
ECHO ��յ�ǰ·�ɱ����Ӽ�¼,��Ҫʹ�ù���ԱȨ�����б�bat
arp -d
for /L %%j IN (101,1,233) DO ping -w 2 -n 1 192.168.1.%%j
for /f "skip=3 tokens=1,* delims= " %%i in ('arp -a') do ECHO IP�� %%i ����·�ɱ���
ECHO.
ECHO ��ѯ��ϣ���������˳�...
pause>nul