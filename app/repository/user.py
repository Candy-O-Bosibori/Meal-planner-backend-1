from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..encryption import Encryption

def create(request: schemas.User, db: Session):
    new_user = models.User(name=request.name, email=request.email, password=Encryption.encrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# def get(user_id: int, db: Session):
#     user = db.query(models.User).filter(models.User.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
#     return user