from fastapi import FastAPI
from .models import Base
from .database import engine
from .routes import user
from .routes import auth
from .routes import products
from .routes import cart
from .routes import feedback


Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(products.router)
app.include_router(cart.router)
app.include_router(feedback.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}