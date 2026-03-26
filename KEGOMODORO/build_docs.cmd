@echo off
cd /d "C:\Users\ariba\OneDrive\Documenti\Software Projects\AI Projects\kegomodoro\KEGOMODORO"
call build_venv\Scripts\pyinstaller.exe --noconfirm --distpath dist_docs --workpath build_docs main.spec
