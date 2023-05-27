from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from hashlib import sha256
from models import User, Credentials, RestoreData

SQL_URL = "sqlite:///./database.db"
Base = declarative_base()


class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    username = Column(String)
    # is_active = Column(Boolean, default=True)
    items = relationship("ItemDB", back_populates="owner")

    def __repr__(self):
        return f"<User(id='{self.id}', email={self.email}, hashed_password={self.hashed_password}, username={self.username})>"


class ItemDB(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("UserDB", back_populates="items")

    def __repr__(self):
        return f"<Item(id='{self.id}', title={self.title}, description={self.description})>"


class CodeDB(Base):
    __tablename__ = "codes"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    code = Column(String)
    is_active = Column(Boolean)
    def __repr__(self):
        return f"<Code(id='{self.id}', email={self.email}, code={self.code}, is_active={self.is_active})>"


def get_hash(text: str) -> str:
    return sha256(text.encode()).hexdigest()



def get_usr(user: [UserDB]) -> User:
    return User(id=user.id, email=user.email, username=user.username, hashed_password=user.hashed_password)


class Database:
    def __init__(self, sql_db_url: str):
        engine = create_engine(sql_db_url, echo=False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def get_users_db(self):
        users = self.session.query(UserDB).all()
        return users

    def add_user(self, creds: Credentials) -> User:
        newUser = UserDB(email=creds.email, hashed_password=get_hash(creds.password))
        self.session.add(newUser)
       self.session.commit()
        return User(id=newUser.id, email=newUser.email, hashed_password=newUser.hashed_password,
                    username=newUser.username)

    def update_user_db(self, user_data: User) -> User:
        user = self.session.query(UserDB).filter_by(id=user_data.id).first()
        user.username = user_data.username
        user.email = user_data.email
        user.hashed_password = user_data.hashed_password
        self.session.commit()
        return get_usr(user)

    def restore_user_db(self, data: RestoreData, password: str) -> User | bool:
        user = self.session.query(UserDB).filter_by(id=id).first()
        code_db = self.session.query(CodeDB).filter_by(email=data.email).first()
        if code_db.is_active:
            print('wow')
            user.hashed_password = get_hash(password)
            self.session.commit()
            return get_usr(user)
        else:
            return False

    def write_code(self, data: RestoreData) -> None:
        code_db = CodeDB(email=data.email, code=data.code)
        self.session.add(code_db)
        self.session.commit()

    def redeem_code(self, data: RestoreData) -> True | False:
        code_db = self.session.query(CodeDB).filter_by(email=data.email).first()
        if code_db.code == data.code:
            code_db.is_active = True
            self.session.commit()
            return True
        else:
            return False


database = Database(SQL_URL)
