@echo off
:: echo %1%
for /F %%i in ('git describe --tags --always --abbrev^=0 HEAD') do (set tagid=%%i)
:: echo %tagid%
set "path=%1%
set "path=%path:/=\%"
:: echo %path%
@echo on
del %path%\dmd_uav(%tagid%).bin /q
ren %path%\dmd_uav.bin dmd_uav(%tagid%).bin


