from fastapi import FastAPI

app = FastAPI()

from app.database import Base, engine
from app.routers import calculator, todo

Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "HelloWorld"}

app.include_router(calculator.router)
app.include_router(todo.router)

