from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, HTTPException, Path
import models
from models import Todos
from database import engine, SessionLocal
from starlette import status
from .auth import get_current_user

router = APIRouter(
    prefix="/admin", # this is the url prefix
    tags=["admin"] # this is the tag to group this router in the docs
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/todo",status_code=status.HTTP_200_OK)
async def read_all(user:user_dependency,db: db_dependency):
    if user is None or user.get("user_role") != "admin":
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
    return db.query(Todos).all()

@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user:user_dependency,db:db_dependency, todo_id: int=Path(gt=0)):
    if user is None or user.get("user_role") != "admin":
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
    todo_model= db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        return HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo_model)
    db.commit()