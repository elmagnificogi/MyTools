@echo off
:start
echo ȷ���㵱ǰJ-Link�����������������ӵ��˶�Ӧ�Ľӿ���
set "answer=0"
echo ����س���ʼ��д
set /p answer=
JLink.exe <F767MCU.txt
echo ע��鿴������Ϣ���Ƿ��� Failed
echo ���������ˢ����ȷ�������successful
echo ��ȷ��д:���������֮������дʱ����ʾ
echo �����ʾskipped ��ʾ���й̼��͵�ǰ��ͬ
echo ȫ��ˢ��֮��ϵ��������۲��Ƿ�ָʾ������
goto start