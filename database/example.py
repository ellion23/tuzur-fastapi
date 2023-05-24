from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from hashlib import sha256

engine = create_engine('sqlite:///example.db', echo=False)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    hashed_password = Column(String)

    def __repr__(self):
        return f"<User(id='{self.id}', name={self.name}, hashed_password={self.hashed_password})>"


def get_hash(text: str) -> str:
    return sha256(text.encode()).hexdigest()


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

user = User(name='Alice', hashed_password=get_hash("abvgd"))
session.add(user)
session.commit()

# Получение всех записей из таблицы
users = session.query(User).all()
print(users)

# Изменение записи в таблице
user = session.query(User).filter_by(name='Alice').first()
user.hashed_password = get_hash('ellionld')
session.commit()

# Удаление записи из таблицы
user = session.query(User).filter_by(name='Alice').first()
session.delete(user)
session.commit()
