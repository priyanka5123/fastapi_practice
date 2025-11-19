from fastapi import FastAPI

app = FastAPI()

from app.routers import calculator


@app.get("/")
async def root():
    return {"message": "HelloWorld"}

app.include_router(calculator.router)


# @app.get("/add")
# def add(a: float=0, b: float=0):
#     return {"result": a+b}

# @app.get("/multiply")
# def multiply(a: float=0, b: float=0):
#     return {"result": a * b}