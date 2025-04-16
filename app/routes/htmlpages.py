from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx

router = APIRouter(tags=["html"])

templates = Jinja2Templates(directory="app/templates")

@router.get("/register", response_class=HTMLResponse)
def get_register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.get("/login", response_class=HTMLResponse)
def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://dummyjson.com/products?limit=20")
        products = response.json().get("products", [])
    return templates.TemplateResponse("home.html", {"request": request, "products": products})


@router.get("/cart-page", response_class=HTMLResponse)
def cart_page(request: Request):
    return templates.TemplateResponse("cart.html", {"request": request})

@router.get("/feedbacks", response_class=HTMLResponse)
def feedback_page(request: Request):
    return templates.TemplateResponse("feedback.html", {"request": request})