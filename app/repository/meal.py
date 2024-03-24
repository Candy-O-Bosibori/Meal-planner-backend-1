from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas

def get(db: Session):
    meals = db.query(models.Meal).all()
    return meals

def create(request: schemas.Meal, db: Session):
    new_meal = models.Meal(image=request.image, title=request.title, time=request.time, serves=request.serves, ingredients=request.ingredients, recipe=request.recipe, nutrition=request.nutrition)
    db.add(new_meal)
    db.commit()
    db.refresh(new_meal)
    return new_meal

def delete(meal_id: int, db: Session):
    meal = db.query(models.Meal).filter(models.Meal.id == meal_id)
    if not meal.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Meal with id {meal_id} not found")
    meal.delete(synchronize_session=False)
    db.commit()
    return "done"

def update(meal_id: int, request: schemas.Meal, db: Session):
    meal = db.query(models.Meal).filter(models.Meal.id == meal_id)
    if not meal.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Meal with id {meal_id} not found")
    meal.update(request.model_dump())
    db.commit()
    return "updated"

def get_meal(meal_id: int, db: Session):
    meal = db.query(models.Meal).filter(models.Meal.id == meal_id).first()
    if not meal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Meal with id {meal_id} not available")
    return meal
