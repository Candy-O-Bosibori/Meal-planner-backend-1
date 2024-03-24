from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import database, schemas
from ..repository import user
from ..oauth2 import get_current_user

router = APIRouter(
    prefix="/user",
    tags=['users']
)
get_db = database.get_db

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

# @router.get("/{user_id}", response_model=schemas.ShowUser)
# def get_user(user_id: int, db: Session = Depends(get_db)):
#     return user.get(user_id, db)

@router.get("/me", response_model=schemas.ShowUser)
def get_current_user_route(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return current_user