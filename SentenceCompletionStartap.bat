@echo off
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -Command "cd '%CD%'; python SentenceCompletion.py"
exit