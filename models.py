from sqlalchemy import Column, Integer, String, ARRAY
from database import Base
from typing import Union

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    user_email = Column(String)
    age = Column(Integer, nullable=True)
    recommendations = Column(ARRAY(String))
    ZIP = Column(Integer, nullable=True)

