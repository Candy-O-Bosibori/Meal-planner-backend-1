from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas

def create(request: schemas.Preferences, user_id: int, db: Session):
    new_preference = models.Preferences(allergens=request.allergens, dietary_type=request.dietary_type, user_id=user_id)
    db.add(new_preference)
    db.commit()
    db.refresh(new_preference)
    return new_preference
    
def get(db: Session):
    preferences = db.query(models.Preferences).all()
    return preferences

def get_one(preference_id: int, db: Session):
    preference = db.query(models.Preferences).filter(models.Preferences.id == preference_id).first()
    if not preference:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Preference with id {preference_id} not found")
    return preference

def update(preference_id: int, request: schemas.Preferences, db: Session):
    preference = db.query(models.Preferences).filter(models.Preferences.id == preference_id)
    if not preference.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Preference with id {preference_id} not found")
    preference.update(request.model_dump())
    db.commit()
    return "updated"