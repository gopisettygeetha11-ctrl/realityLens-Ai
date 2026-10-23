@echo off
echo Starting RealityLens AI - Delivery Apps...
call .venv\Scripts\activate.bat 2>nul
streamlit run delivery_apps\app.py
pause
