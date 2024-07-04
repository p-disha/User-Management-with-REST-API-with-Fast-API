from sqlalchemy import Boolean, Column, Integer, String
from database import Base, engine

# Create a new User class and inherit it from the Base class present in the /usercode/Application/database.py file.
# Add the following class variables to this class: 
Base.metadata.create_all(engine)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    country = Column(String)
    isActive = Column(Boolean)
    hashed_password = Column(String)
Base.metadata.create_all(engine)