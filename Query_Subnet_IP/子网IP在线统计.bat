:::::::�鿴��������IP.bat:::::::
@echo off
title �鿴��������IP
 
set /a Online=0
set /a Offline=0
set /a Total=256
set ExportFile=����IP����ͳ��.txt
:: ��ʼ������IP�벻����IP�ĸ���Ϊ�㣬��ɨ��256��IP�����������ļ���
 
set StartTime=%time%
:: ��¼����Ŀ�ʼʱ��
 
for /f "delims=: tokens=2" %%i in ('ipconfig /all ^| find /i "IPv4"') do set IP=%%i
:: ��ñ���IP [ע1]
 
if "%IP%"=="" echo δ���ӵ����� & pause & goto :EOF
if "%IP%"==" 0.0.0.0" echo δ���ӵ����� & pause & goto :EOF
:: ��IPΪ�ջ� 0.0.0.0 ʱ����ʾδ���Ӳ��˳��ó���
 
for /f "delims=. tokens=1,2,3,4" %%i in ("%IP%") do (
  set /a IP1=%%i
  set /a IP2=%%j
  set /a IP3=%%k
  set /a IP4=%%l
)
:: ������ʵ�����޸Ĳ�ѯ��IP���� ����ѭ��ֱ���޸�
:: �Ծ��Ϊ�ָ������ֱ�IP���ĸ�ʮ�����������ĸ�����

echo %IP1%
echo %IP2%
echo %IP3%
echo %IP4%
 
set /a IP4=0
echo ���ߵ�IP��>%ExportFile%
:: ��ʼ��IP�ĵ��ĸ���ֵΪ0���������������ļ�,��Ҫ��ѯ�����������
 
:RETRY
ping %IP1%.%IP2%.%IP3%.%IP4% -n 1 -w 200 -l 16>nul && set /a Online+=1 && echo %IP1%.%IP2%.%IP3%.%IP4%>>%ExportFile% || set /a Offline+=1
:: ping Ŀ��IP [ע2]
 

set /a Scanned=%Online%+%Offline%
set /a Progress=(%Online%+%Offline%)*100/%Total%
echo ����ɨ�裺%Scanned%/%Total% ɨ����ȣ�%Progress%%%
 
set /a IP4+=1
:: ÿ�β�ѯ�Ĳ���������
if %IP4% lss %Total% goto :RETRY
:: ��IP�ĵ��ĸ���ֵС������ʱ����ת�� :RETRY �����ظ�ִ��ֱ��ȫ�� ping ��Ϊֹ
 
echo.
echo.
 
set EndTime=%time%
:: ��¼����Ľ���ʱ��
 
set /a Seconds = %EndTime:~6,2% - %StartTime:~6,2%
set /a Minutes = %EndTime:~3,2% - %StartTime:~3,2%
if %Seconds% lss 0 set /a Seconds += 60 & set /a Minutes -= 1
if %Minutes% lss 0 set /a Minutes += 60
:: ����ʱ���
 
set /a Percent=%Online%*100/(%Online%+%Offline%)
:: �������߰ٷֱ�
 
echo ����IP����:  %Online%
echo ������IP����: %Offline%
echo ���߰ٷֱ�:  %Percent%%%
echo ͳ�ƺ�ʱ:   %Minutes%��%Seconds%��
echo ͳ������:   %date% %time:~0,-3%
echo.>>%ExportFile%
echo ����IP����:  %Online%>>%ExportFile%
echo ������IP����: %Offline%>>%ExportFile%
echo ���߰ٷֱ�:  %Percent%%%>>%ExportFile%
echo ͳ�ƺ�ʱ:   %Minutes%��%Seconds%��>>%ExportFile%
echo ͳ������:   %date% %time:~0,-3%>>%ExportFile%
echo ��¼�ѱ��浽�ļ�"%ExportFile%"��
::��ʾ�������������浽�ļ���
pause