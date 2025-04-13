from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from ..schema import UserLogin
from ..models import User
from ..utils import verify
from ..oauth2 import create_acess_token, get_current_user

router = APIRouter(tags =['Authentication'])

@router.post("/login")
def login(user_credentials : OAuth2PasswordRequestForm = Depends(),db : Session = Depends(get_db)):
    
    user = db.query(User).filter(User.email == user_credentials.username).first()
   
    if not user:
        print("user not found")
    
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
        
    if not verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"invalid credentials")
    
    access_token = create_acess_token(data = {"user_id":str(user.user_id)})
    return {"access_token" : access_token, "token_type" : "bearer" }

@router.get("/me")
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user