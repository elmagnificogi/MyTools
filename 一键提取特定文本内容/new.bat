type a.txt|find "Raw bytes:01" >>rawdata.txt;
for /f "delims=" %%a in (rawdata.txt) do (
      set ip=%%a

echo %ip:~44,6%
set high = 0
set low  = 0
set /a high = %ip:~44,2%
set /a "high = 0x%high%"
set /a low  = %ip:~47,2%
set /a "low = 0x%low%"

    )
echo %high
echo %low
    pause>nul