for /F %%i in ('git describe --tags --always --abbrev^=0 HEAD') do (set tagid=%%i)
echo %tagid%
set num=%tagid:~-3%
echo #include "version.h" > ./rtos/start/version.c
echo.>> ./rtos/start/version.c
echo //File generated by automatically. Any manual change will be rewritten >> ./rtos/start/version.c
echo.>> ./rtos/start/version.c
echo const char * g_firmware_id = "n2.x.%num%"; >> ./rtos/start/version.c
echo.>> ./rtos/start/version.c