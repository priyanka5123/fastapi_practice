from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Todo(BaseModel):
    id: int 
    task: str 
    completed: bool = False

todos = []

@router.post("/todo")
def create_item(todo: Todo):
    todos.append(todo)
    return {"status": "created", "todo": todo}

@router.get("/todo")
def get_items():
    return todos

@router.put("/todo/{todo_id}")
def update_item(todo_id: int, updated: Todo):
    for i, t in enumerate(todos):
        if t.id == todo_id:
            todos[i] = updated
            return {"status": "updated", "todo": updated}
    return {"error": "not found"}

@router.delete("/todo/{todo_id}")
def delete_item(todo_id: int):
    global todos
    todos = [t for t in todos if t.id != todo_id]
    return {"status": "deleted"}
