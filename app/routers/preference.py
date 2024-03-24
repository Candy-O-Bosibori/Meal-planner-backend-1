from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import database, schemas, oauth2
from ..repository import preference

router = APIRouter(
    prefix="/preference",
    tags=['preferences']
)
get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_preference(request: schemas.Preferences, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    if current_user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not authenticated")
    return preference.create(request, current_user.id, db)

@router.get('/')
def get_preferences(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return preference.get(db)

@router.get('/{preference_id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowPreferences)
def get_preference(preference_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return preference.get_one(preference_id, db)

@router.put('/{preference_id}', status_code=status.HTTP_202_ACCEPTED)
def update_preference(preference_id: int, request: schemas.Preferences, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return preference.update(preference_id, request, db)