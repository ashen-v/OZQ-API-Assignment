from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

engine = create_engine("postgresql+psycopg://postgres:0000@localhost:5432/ozqdatabase")

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

# Dependency function
def get_db():
    db = SessionLocal()
    try:
        yield db  # Provide database session
    finally:
        db.close()  # Ensure the session is closed

