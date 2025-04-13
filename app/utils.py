from passlib.context import CryptContext

#standard  boilerplate for utilaizing  passlib bvrypt algorithem
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

#hash plaintext passwords
def hash(password: str):
    return pwd_context.hash(password)

#compare attempt password with hashpassword in database
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password,hashed_password)
