python -m venv venv
venv/Scripts/activate
        pip install "fastapi[standard]"
        pip install uvicorn

run cd app fastapi dev main.py
run uvicorn app.main:app --reload(Run Uvicorn from project root)
http://127.0.0.1:8000/add?a=10&b=20
http://127.0.0.1:8000/multiply?a=5&b=6

http://127.0.0.1:8000/docs or postman
http://127.0.0.1:8000/todo get
POST http://127.0.0.1:8000/todo
{
  "id": 1,
  "task": "Learn FastAPI project",
  "completed": false
}
PUT http://127.0.0.1:8000/todo/1
{
  "id": 1,
  "task": "Do FastAPI project",
  "completed": false
}
Delete http://127.0.0.1:8000/todo/1

for db pip install sqlalchemy
for jwt pip install python-jose passlib[bcrypt]

To generate secret key in powershell
[guid]::NewGuid().ToString()
pip install dotenv
pip uninstall bcrypt passlib -y
pip install passlib[bcrypt]
pip install argon2_cffi
POST /register
{
  "username": "sara",
  "password": "s123"
}
POST /login
{
  "username": "sara",
  "password": "s123"
}
response
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}

curl -H "Authorization: Bearer <access_token>" http://127.0.0.1:8000/me
response
{ "username": "sara" }
