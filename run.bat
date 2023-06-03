@echo off
set PYCHARM_PATH="C:\Program Files\JetBrains\PyCharm Community Edition 2022.2.4\bin\pycharm.exe"
set PROJECT_PATH="D:\selenium projects\frameworks\Advarisk"
set COMMAND="pytest -s -v -m 'sanity' --html=.Reports\report.html TestCases\ --browser firefox"
start %PYCHARM_PATH% %PROJECT_PATH% %COMMAND%
