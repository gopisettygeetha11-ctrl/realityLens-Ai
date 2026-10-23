@echo off
echo Starting RealityLens AI - Places App...
call .venv\Scripts\activate.bat 2>nul
streamlit run ai_places_app\app.py
pause
