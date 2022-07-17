@echo off
cd /d "%~dp0"
echo 温馨提示：若电视执行脚本后异常，恢复方法“关电视，拔电源，等十秒后，然后插电源，同时按住遥控器主页键和菜单键不放，开电视，然后进入recovery，清除数据后重启，就会恢复原厂设置了。
echo 打开设置-关于-产品型号，对着产品型号连点七次，开发模式就开启了，之后返回账号与安全，找到adb调试，并打开，接着进入网络设置，记住自己的IP地址

set /p var=按回车键继续：

echo 请输入电视IP地址，按回车键确认，此时电视会提示是否连接电脑，选择确认即可；
set /p ip=电视IP地址:

echo 正在连接，请稍后
set matchStr=connected
:connect
for /f "tokens=*" %%i in ('%~dp0adb connect %ip%') do @set  result=%%i

echo %result% | findstr %matchStr% >nul && (echo 连接成功) || (echo 连接失败，正在重试
  (goto connect))

echo 正在精简中，耐心等待。。。

adb shell pm uninstall --user 0 com.xiaomi.mitv.tvpush.tvpushservice

adb shell pm uninstall --user 0 com.xiaomi.mitv.advertise

adb shell pm uninstall --user 0 com.miui.systemAdSolution

adb shell pm uninstall --user 0 com.xiaomi.mibox.gamecenter


echo "恭喜您，精简成功，快去重启下电视，看看效果吧！"

@pause