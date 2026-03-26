@echo off
cd /d "C:\Users\ariba\OneDrive\Documenti\Software Projects\AI Projects\kegomodoro\KEGOMODORO"
call build_venv\Scripts\pyinstaller.exe --noconfirm --distpath dist_core --workpath build_core main.spec
copy /Y .env.example dist_core\.env.example >nul
