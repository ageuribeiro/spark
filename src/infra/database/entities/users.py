from sqlalchemy import Column, Integer, String
from src.infra.database import Base


class Users(Base):
    """Users Entity"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return f"User: name={self.first_name} {self.last_name}, age={self.age}]"
