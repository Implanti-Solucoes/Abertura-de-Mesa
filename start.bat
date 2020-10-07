CALL venv\Scripts\activate.bat
set FLASK_APP=main.py
python -m flask run --host=%computername% --port=8182