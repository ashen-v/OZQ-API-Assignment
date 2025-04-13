from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String, nullable=False)
    email  = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

class CartItem(Base):
    __tablename__ = "cart_items"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    product_id = Column(Integer)
    product_title = Column(String)
    quantity = Column(Integer, default=1)

class FeedBack(Base):
    __tablename__= "feedback"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    feedback = Column(String, nullable=False)
