from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.todo_model import Todo as TodoModel

router = APIRouter()

# Pydantic schema
class TodoSchema(BaseModel):
    task: str
    completed: bool = False

class TodoResponse(BaseModel):
    id: int
    task: str
    completed: bool

    class Config:
        orm_mode = True


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE
@router.post("/todo", response_model=TodoResponse)
def create_todo(todo: TodoSchema, db: Session = Depends(get_db)):
    new_todo = TodoModel(task=todo.task, completed=todo.completed)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


# READ ALL
@router.get("/todo", response_model=list[TodoResponse])
def list_todos(db: Session = Depends(get_db)):
    return db.query(TodoModel).all()


# UPDATE
@router.put("/todo/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo: TodoSchema, db: Session = Depends(get_db)):
    existing = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Todo not found")

    existing.task = todo.task
    existing.completed = todo.completed

    db.commit()
    db.refresh(existing)
    return existing


# DELETE
@router.delete("/todo/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    existing = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(existing)
    db.commit()
    return {"status": "deleted"}
