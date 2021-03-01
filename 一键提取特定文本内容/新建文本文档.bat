@echo off & color 0e & setlocal enabledelayedexpansion 
  ipconfig>ip.txt 
    for /f "delims=" %%a in (ip.txt) do ( 
      for /f "tokens=1* delims=:" %%i in ('call echo %%a^|find /i "IPv4 µØÖ·"') do (
     Echo %%a>>"1.txt"
        )  
    ) 
 del /s /q ip.txt & start 1.txt
 exit