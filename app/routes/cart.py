from fastapi import HTTPException, status, Depends, APIRouter, Response
from sqlalchemy.orm import Session
from ..database import get_db
from ..schema import Cart
from ..models import CartItem
from ..oauth2 import get_current_user



router = APIRouter(prefix="/cart",tags=["cart"])


#add items to cart
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Cart)
def add_cart(cart: Cart, db: Session = Depends(get_db), user=Depends(get_current_user)):

    cart.user_id = user.user_id
    new_cart = CartItem(**cart.model_dump())
    db.add(new_cart)
    db.commit()
    db.refresh(new_cart)
    return new_cart


# get users cart
@router.get("/", response_model=list[Cart])
def get_my_cart(db: Session = Depends(get_db), user=Depends(get_current_user)):
    cart_items = db.query(CartItem).filter(CartItem.user_id == user.user_id).all()
    return cart_items


#delete cart
@router.delete("/{id}")
def delete_cart(id : int, db: Session = Depends(get_db), user=Depends(get_current_user)):

    cart = db.query(CartItem).filter(CartItem.user_id == id).first()
    if not cart:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"cart not found")
    cart.delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)