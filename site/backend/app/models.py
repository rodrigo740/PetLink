from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    userName = Column(String)
    address = Column(String)
    contact = Column(String)
    name = Column(String)
    birthday = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
