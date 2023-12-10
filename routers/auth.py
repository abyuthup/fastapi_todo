from datetime import timedelta,datetime
from http.client import HTTPException
from typing import Annotated
from pydantic import BaseModel
from database import SessionLocal
from fastapi import APIRouter,Depends
from models import Users
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import  jwt, JWTError


router = APIRouter(
    prefix="/auth", # this is the url prefix
    tags=["auth"] # this is the tag to group this router in the docs
)

# openssl rand -hex 32
SECRET_KEY = "fbd5222323f304be0e3859cce2248cb7ab20bc86846951b0a1b7cbfb62ff581a"
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]




class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str

class Token(BaseModel):
    access_token: str
    token_type: str

def authenticate_user(db: db_dependency, username: str, password: str):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(user_name:str,user_id:int,expires_delta:timedelta):
    to_encode = {"sub": user_name, "id": user_id}
    expires = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expires})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str,Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
        return {"username": username, "id": user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db:db_dependency,create_user_request: CreateUserRequest):
    create_user_model = Users(username=create_user_request.username,
                            email=create_user_request.email,
                            first_name=create_user_request.first_name,
                            last_name=create_user_request.last_name,
                            hashed_password=bcrypt_context.hash(create_user_request.password),
                            role=create_user_request.role,
                            is_active=True
                            )
    db.add(create_user_model)
    db.commit()


@router.post("/token", response_model=Token)
async def login_for_access_token(db: db_dependency, form_data:Annotated[OAuth2PasswordRequestForm,Depends()]):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
    access_token = create_access_token(user.username,user.id,timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}
    