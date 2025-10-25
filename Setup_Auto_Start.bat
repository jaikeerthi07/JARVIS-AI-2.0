@echo off
title Setup JARVIS Auto Start

echo ========================================
echo Setting up JARVIS Auto Start
echo ========================================

REM Change to the jarvis directory
cd /d "c:\Users\Jaikeerthi\Music\jarvis\jarvis"

echo Creating scheduled task to start JARVIS at logon...
powershell -ExecutionPolicy Bypass -File "start_jarvis_task.ps1"

echo.
echo JARVIS Auto Start Setup Complete!
echo JARVIS will now start automatically when you log into Windows.
echo.
pause