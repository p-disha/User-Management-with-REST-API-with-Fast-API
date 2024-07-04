from sqlalchemy.orm import Session
from sqlalchemy import update
import models, schemas

# Create a get_users() method in the /usercode/Application/crud.py file to fetch the records from the database and return them to the calling function.

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# fetch the records from the database.
# Fetch all the records from the database.
# Filter the results on the base of the ID.
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# fetch the records from the database.
# Fetch all the records from the database.
# Filter the results on the base of the email.

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


# Accepts the instance of a session and user.
# Hashes the password to store it in the database.
# Creates a new user using the model and adds it to the database using the session.


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = hash(user.password)
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password
                        ,username = user.username, first_name = user.first_name, last_name = user.last_name,
                        gender = user.gender, country = user.country, isActive = user.isActive)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    
# Create an update_user() function in the /usercode/Application/crud.py file that does the following:
# Searches for the user using the email of the user.
# Updates the records of the user based on the new values passed by the user to the API.
# Updates the records in the database.


def update_user(db: Session, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    for field in user.__dict__:
        setattr(db_user, field, getattr(user, field))
    db.commit()
    db.refresh(db_user)
    return db_user

# Create a delete_user() method in the /usercode/Application/crud.py file that accepts the user_id and deletes the user from the database.

def delete_user(db: Session, user_id: int):
    record_obj = db.query(models.User).filter(models.User.id==user_id).first()
    db.delete(record_obj)
    db.commit()
    return record_obj