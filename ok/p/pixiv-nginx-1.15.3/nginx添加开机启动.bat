@echo off
color 0A
echo .
echo ���������ӿ�������: %cd%\start-nginx.exe
echo ���ɱ��������أ���������
echo .
pause
echo .
echo ִ����....
echo .
@reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v "nginx-pixiv" /d "\"%cd%\start-nginx.exe\""
echo .
echo �ѳ�����ӿ�������������ʾ�ܾ����ʣ�����ɱ��������ػ�ϵͳȨ�޲���
echo .
pause