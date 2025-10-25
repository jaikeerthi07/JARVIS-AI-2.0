JARVIS AUTOMATIC STARTUP INSTRUCTIONS
=====================================

This package includes several ways to automatically start JARVIS:

1. DOUBLE-CLICK STARTUP:
   - Double-click "Start_JARVIS.bat" to launch JARVIS manually
   - This is the simplest way to start JARVIS on demand

2. AUTO-START AT WINDOWS LOGON:
   - Run "Setup_Auto_Start.bat" to create a scheduled task
   - This will make JARVIS start automatically when you log into Windows
   - To remove auto-start, go to Task Scheduler and delete the "JARVIS Assistant" task

3. FILES INCLUDED:
   - launch_jarvis.py: Main Python script to launch JARVIS
   - Start_JARVIS.bat: Double-clickable batch file to start JARVIS
   - Setup_Auto_Start.bat: Sets up automatic startup at logon
   - start_jarvis_task.ps1: PowerShell script for scheduled task creation

4. WEB INTERFACE ACCESS:
   - Once JARVIS is running, access the web interface at:
     http://localhost:8002 (if using the Python HTTP server)
   - The default port may vary depending on availability

5. VOICE COMMANDS:
   - Press Ctrl+J to toggle voice recognition on/off
   - Say "activated jarvis to reddot" to activate red mode
   - Say "jarvis normal mode" to return to normal mode

6. TROUBLESHOOTING:
   - If JARVIS doesn't start, check that Python is installed and in your PATH
   - Make sure all required packages are installed (pip install -r requirements.txt)
   - If there are port conflicts, JARVIS will automatically try different ports

Enjoy your JARVIS Assistant!