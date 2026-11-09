@echo off
cd /d "%~dp0"
echo ===================================================
echo Starting Abrham Mosye Belsty's Portfolio Website...
echo ===================================================
call "venv\Scripts\activate.bat"
streamlit run app.py
pause
