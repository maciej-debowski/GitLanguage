@echo off
title Git Shell
color a
cls
:shell
py shell.py
color 4
echo Git Shell Crashed! :/ 
echo All Git datas ( variables, arrays, functions ) was deleted :( !
echo Press any key to restart shell!
Pause>nul
cls
color a
goto shell