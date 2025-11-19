from fastapi import APIRouter

router = APIRouter()

@router.get("/add")
def add(a: float=0, b: float=0):
    return {"result": a+b}

@router.get("/multiply")
def multiply(a: float=0, b: float=0):
    return {"result": a*b}