from fastapi import FastAPI

app = FastAPI()

from app.routers import calculator, todo


@app.get("/")
async def root():
    return {"message": "HelloWorld"}

app.include_router(calculator.router)
app.include_router(todo.router)

