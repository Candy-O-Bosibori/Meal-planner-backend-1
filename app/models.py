from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Meal(Base):
    
    __tablename__ = "meals"
    
    id = Column(Integer, primary_key=True, index=True)
    image = Column(String)
    title = Column(String)
    time = Column(String)
    serves = Column(Integer)
    ingredients = Column(JSON)
    recipe = Column(JSON)
    nutrition = Column(JSON)
    
class User(Base):
    
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)
    
    preferences = relationship("Preferences", back_populates="owner")
    
class Preferences(Base):
    
    __tablename__ = "preferences"
    
    id = Column(Integer, primary_key=True, index=True)
    allergens = Column(String)
    dietary_type = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="preferences")