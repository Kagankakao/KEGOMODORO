@echo off
cd /d "C:\Users\ariba\OneDrive\Documenti\Software Projects\AI Projects\kegomodoro\KEGOMODORO"
call build_venv\Scripts\pyinstaller.exe --noconfirm --distpath dist_notes --workpath build_notes main.spec
