from pydantic import BaseModel
from typing import List, Dict, Union, Optional

class Meal(BaseModel):
    image: str
    title: str
    time: str
    serves: int
    ingredients: List[Union[str, int]]
    recipe: List[Union[str, int]]
    nutrition: Dict[str, Union[str, int]]
    
    
class ShowMeal(BaseModel):
    class Config:
        orm_mode = True
        
class User(BaseModel):
    email: str
    password: str
    
class Preferences(BaseModel):
    allergens: str
    dietary_type: str
    
    class Config:
        orm_mode = True
    
class ShowUser(BaseModel):
    email: str
    preferences : List[Preferences] = []
    
    class Config:
        orm_mode = True
        
class ShowPreferences(BaseModel):
    allergens: str
    dietary_type: str
    owner: ShowUser
    
    class Config:
        orm_mode = True
        
class Login(BaseModel):
    username: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None