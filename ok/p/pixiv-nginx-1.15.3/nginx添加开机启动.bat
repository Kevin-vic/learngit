@echo off
color 0A
echo .
echo 按任意键添加开机启动: %cd%\start-nginx.exe
echo 如果杀毒软件拦截，请点击允许
echo .
pause
echo .
echo 执行中....
echo .
@reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v "nginx-pixiv" /d "\"%cd%\start-nginx.exe\""
echo .
echo 已尝试添加开机启动，如显示拒绝访问，就是杀毒软件拦截或系统权限不够
echo .
pause