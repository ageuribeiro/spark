"""This module contains the Issue entity."""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.database import Base

class Issue(Base):
  
    """Issue Entity."""

    __tablename__ = "issues"

    id = Column(Integer, primary_key=True)
    operacao = Column(String, nullable=False)
    body = Column(String, nullable=False)
    status = Column(String, nullable=False)
    tt_primesys = Column(String, nullable=False)
    incident = Column(String, nullable=False)
    id_queues = Column(Integer, ForeignKey("queues.id"), nullable=False)

    def __repr__(self):
        return f"Issue [operacao={self.operacao}, body={self.body}, status={self.status}, tt_primesys={self.tt_primesys}, id_queues={self.id_queues}]"

    