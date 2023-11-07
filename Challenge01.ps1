@echo off

REM Require admin rights to run this script
REM ======================================

REM Check for admin rights 
net session >nul 2>&1
if %errorLevel% == 0 (
  echo Success: Admin rights confirmed.
) else (
  echo Error: This script requires admin rights to run.
  exit /b 1 
)

REM Enable automatic updates
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" /v NoAutoUpdate /t REG_DWORD /d 0 /f

REM Set update check frequency to daily
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" /v ScheduledInstallDay /t REG_DWORD /d 0 /f

REM Enable automatic install of updates 
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" /v ScheduledInstallTime /t REG_DWORD /d 3 /f

echo Automatic OS updates have been enabled on this machine.