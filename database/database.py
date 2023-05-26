from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from hashlib import sha256
from models import User, Credentials

SQL_URL = "sqlite:///./database.db"
Base = declarative_base()


class User_db(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    username = Column(String)
    # is_active = Column(Boolean, default=True)
    items = relationship("Item_db", back_populates="owner")

    def __repr__(self):
        return f"<User(id='{self.id}', email={self.email}, hashed_password={self.hashed_password}, username={self.username})>"


class Item_db(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User_db", back_populates="items")

    def __repr__(self):
        return f"<Item(id='{self.id}', title={self.title}, description={self.description})>"


class Database:
    def __init__(self, sql_db_url: str):
        engine = create_engine(sql_db_url, echo=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def get_users_db(self):
        users = self.session.query(User_db).all()
        return users

    def get_usr(self, user: [User_db]) -> User:
        return User(id=user.id, email=user.email, username=user.username, hashed_password=user.hashed_password)

    def get_hash(self, text: str) -> str:
        return sha256(text.encode()).hexdigest()

    def add_user(self, creds: Credentials) -> User:
        newUser = User_db(email=creds.email, hashed_password=self.get_hash(creds.password))
        self.session.add(newUser)
        self.session.commit()
        return User(id=newUser.id, email=newUser.email, hashed_password=newUser.hashed_password,
                    username=newUser.username)

    def update_user_db(self, user_data: User) -> User:
        user = self.session.query(User_db).filter_by(id=user_data.id).first()
        user.username = user_data.username
        user.email = user_data.email
        user.hashed_password = user_data.hashed_password
        self.session.commit()
        return self.get_usr(user)

    def restore_user_db(self, creds: Credentials, id) -> User:  # rewrites pass and email
        user = self.session.query(User_db).filter_by(id=id).first()


database = Database(SQL_URL)
