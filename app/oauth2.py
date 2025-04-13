from jose import jwt, JWTError
from datetime import datetime, timedelta
from .schema import TokenData
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from .models import User
from sqlalchemy.orm import Session
from .database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = 'login')


SECRET_KEY = "b0593e0c69de1e0f56f2ddd9feeb14ab9f81cb6c8bd033a61ed8aff4288aa4ee"

ALGORITHEM = "HS256"

ACESS_TOKEN_EXPIRE_MINUTES  = 300

def create_acess_token(data:dict):

    to_encode =  data.copy()
    expire = datetime.now() + timedelta(minutes=ACESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHEM)
    return encoded_jwt

def verify_acess_token(token: str,credentials_exception):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms= [ALGORITHEM])

        id = payload.get("user_id")

        if id is None:
            raise credentials_exception
        token_data = TokenData(id= id)
    except JWTError:
        raise credentials_exception
    
    return token_data
    
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    
    token_id = verify_acess_token(token, credentials_exception)
    user = db.query(User).filter(User.user_id == int(token_id.id)).first()
    
    if user is None:
        raise credentials_exception
    return user
    