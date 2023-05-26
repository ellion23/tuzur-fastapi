from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# from database.session import get_db
# from schemas.user import UserCreate, User
# from utils.auth import get_current_user, create_access_token, get_password_hash

SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


user = User_db(email='Alice@heh.com', hashed_password=get_hash("abvgd"))
session.add(user)
session.commit()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    # db = SessionLocal()
    # try:
    #     yield db
    # finally:
    #     db.close()
    pass


# db: Session = Depends(get_db)
def get_users_db():
    user = User_db(email='Alice@heh.com', hashed_password=get_hash("abvgd"))
    session.add(user)
    session.commit()
    users = session.query(User_db).all()
    print(users)
    return users
