from sqlalchemy import Column, Integer, String
from src.infra.database import Base


class Queue(Base):
    """Queue Entity."""

    __tablename__ = "queues"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    sigla = Column(String, nullable=False)

    def __repr__(self):
        return f"Queue [name={self.name}, description={self.description}, sigla={self.sigla}]"
