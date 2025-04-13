from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password : str

class UserLogin(BaseModel):
    email : EmailStr
    password : str

class Token(BaseModel):
    acess_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Cart(BaseModel):
    user_id: Optional [int] = None
    product_id: int
    product_title: str
    quantity: int

    class Config:
        from_attributes = True 

class FeedBackitem(BaseModel):
    user_id: Optional [int] = None
    feedback : str
    