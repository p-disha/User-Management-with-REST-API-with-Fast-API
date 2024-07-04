from pydantic import BaseModel
from typing import List

# The main objective of defining the objects using pydantic is to use models. Models are simply classes that inherit the BaseModel class.

# To create a schema for the BaseUser class, which will be mapped to the database, complete the following steps:

# Create a BaseUser class and inherit it from the BaseModel from pyndatic.
# Add the user parameters to this class, except for the id and hashed_password variables.
class UserBase(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    gender: str
    country: str
    isActive: bool



# Create a schema for the User class by creating a class and inheriting it from the UserBase class.
# Create a bridge to the database using this class’s ORM.
# Create another class, UserCreate, inheriting the UserBase class, and store the password for the user.
class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    class Config:
        orm_mode = True