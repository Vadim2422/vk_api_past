from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


class Vk(Base):
    __tablename__ = "vk"

    id = Column(Integer, primary_key=True, nullable=False)
    token = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    id_vk = Column(String, nullable=False)
