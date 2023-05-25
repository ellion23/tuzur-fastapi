from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from sqlalchemy import create_engine
from models import User

Base = declarative_base()

SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)


class User_db(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
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


def add_user(data):
    users = session.query(User_db).all()
    for user in users:
        if user.email == data.email:
            return "already"
    pass
