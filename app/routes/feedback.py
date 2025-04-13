from fastapi import HTTPException, status, Depends, APIRouter, Response
from sqlalchemy.orm import Session
from ..database import get_db
from ..schema import FeedBackitem
from ..models import FeedBack
from ..oauth2 import get_current_user


router = APIRouter(prefix="/feedback", tags=["feedback"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=FeedBackitem)
def add_cart(feedback: FeedBackitem, db: Session = Depends(get_db), user=Depends(get_current_user)):

    feedback.user_id = user.user_id
    new_feedback = FeedBack(**feedback.model_dump())
    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)
    return new_feedback


@router.get("/", response_model=list[FeedBackitem])
def get_feedback(db: Session = Depends(get_db)):
    feedback = db.query(FeedBack).all()
    if not feedback:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"feedback not found")
    return feedback
