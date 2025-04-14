from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .models import Base
from .database import engine
from .routes import user
from .routes import auth
from .routes import products
from .routes import cart
from .routes import feedback
from .routes import htmlpages


Base.metadata.create_all(engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(products.router)
app.include_router(cart.router)
app.include_router(feedback.router)
app.include_router(htmlpages.router)



@app.get("/")
async def root():
    return {"message": "Hello World"}