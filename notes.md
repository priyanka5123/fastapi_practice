python -m venv venv
venv/Scripts/activate
        pip install "fastapi[standard]"
        pip install uvicorn

run cd app fastapi dev main.py
run uvicorn app.main:app --reload(Run Uvicorn from project root)
http://127.0.0.1:8000/add?a=10&b=20
http://127.0.0.1:8000/multiply?a=5&b=6
