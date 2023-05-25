from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from hashlib import sha256
from models import User, Credentials

Base = declarative_base()

SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)


class User_db(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    username = Column(String)
    # is_active = Column(Boolean, default=True)
    items = relationship("Item_db", back_populates="owner")

    def __repr__(self):
        return f"<User(id='{self.id}', email={self.email}, hashed_password={self.hashed_password})>"


class Item_db(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User_db", back_populates="items")

    def __repr__(self):
        return f"<Item(id='{self.id}', title={self.title}, description={self.description})>"


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def get_users_db():
    users = session.query(User_db).all()
    return users


def get_hash(text: str) -> str:
    return sha256(text.encode()).hexdigest()


def add_user(creds: Credentials):
    newUser = User_db(email=creds.email, hashed_password=get_hash(creds.password))
    session.add(newUser)
    session.commit()
    return User(id=newUser.id, email=newUser.email, hashed_password=newUser.hashed_password, username=newUser.username)


def update_user_db(user_data: User):
    user = session.query(User_db).filter_by(id=user_data.id).first()
    user.username = user_data.username
    user.email = user_data.email
    user.hashed_password = user_data.hashed_password
    session.commit()
    return User(id=user.id, username=user.username, email=user.email, hashed_password=user.hashed_password)
