@echo off
cd /d "%~dp0"
echo ��ܰ��ʾ��������ִ�нű����쳣���ָ��������ص��ӣ��ε�Դ����ʮ���Ȼ����Դ��ͬʱ��סң������ҳ���Ͳ˵������ţ������ӣ�Ȼ�����recovery��������ݺ��������ͻ�ָ�ԭ�������ˡ�
echo ������-����-��Ʒ�ͺţ����Ų�Ʒ�ͺ������ߴΣ�����ģʽ�Ϳ����ˣ�֮�󷵻��˺��밲ȫ���ҵ�adb���ԣ����򿪣����Ž����������ã���ס�Լ���IP��ַ

set /p var=���س���������

echo ���������IP��ַ�����س���ȷ�ϣ���ʱ���ӻ���ʾ�Ƿ����ӵ��ԣ�ѡ��ȷ�ϼ��ɣ�
set /p ip=����IP��ַ:

echo �������ӣ����Ժ�
set matchStr=connected
:connect
for /f "tokens=*" %%i in ('%~dp0adb connect %ip%') do @set  result=%%i

echo %result% | findstr %matchStr% >nul && (echo ���ӳɹ�) || (echo ����ʧ�ܣ���������
  (goto connect))

echo ���ھ����У����ĵȴ�������

adb shell pm uninstall --user 0 com.xiaomi.mitv.tvpush.tvpushservice

adb shell pm uninstall --user 0 com.xiaomi.mitv.advertise

adb shell pm uninstall --user 0 com.miui.systemAdSolution

adb shell pm uninstall --user 0 com.xiaomi.mibox.gamecenter


echo "��ϲ��������ɹ�����ȥ�����µ��ӣ�����Ч���ɣ�"

@pause