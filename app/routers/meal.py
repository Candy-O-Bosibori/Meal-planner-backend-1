from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import database, schemas, oauth2
from ..repository import meal


router = APIRouter(
    prefix="/meal",
    tags=['meals']
)
get_db = database.get_db

@router.get("/")
def get_meals(db: Session = Depends(get_db)):
    return meal.get(db)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_meal(request: schemas.Meal, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return meal.create(request, db)
    
@router.delete("/{meal_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_meal(meal_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return meal.delete(meal_id, db)

@router.put("/{meal_id}", status_code=status.HTTP_202_ACCEPTED)
def update_meal(meal_id: int, request: schemas.Meal, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return meal.update(meal_id, request, db)

@router.get("/{meal_id}", status_code=status.HTTP_200_OK)
def get_meal(meal_id: int, db: Session = Depends(get_db)):
    return meal.get_meal(meal_id, db)