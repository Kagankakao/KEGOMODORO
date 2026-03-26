@echo off
cd /d "C:\Users\ariba\OneDrive\Documenti\Software Projects\AI Projects\kegomodoro\KEGOMODORO"
call build_venv\Scripts\pyinstaller.exe --noconfirm --distpath dist_env --workpath build_env main.spec
copy /Y .env.example dist_env\.env.example >nul
