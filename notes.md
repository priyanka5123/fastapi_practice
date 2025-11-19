python -m venv venv
venv/Scripts/activate
        pip install "fastapi[standard]"
        pip install uvicorn

run cd app fastapi dev main.py
uvicorn app.main:app --reload
