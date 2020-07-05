@echo off
	echo. 
	echo.关闭Nginx...... 
	taskkill /F /IM nginx.exe > nul
	echo.OK,关闭所有nginx 进程
echo.按任意键关闭
pause