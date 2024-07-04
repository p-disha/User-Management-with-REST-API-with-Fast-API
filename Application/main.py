from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud
import models
import schemas
from database import SessionLocal, engine


app = FastAPI()

@app.get("/")
async def docs_redirect():
    response = RedirectResponse(url='/docs')
    return response

# Get the local session from the/usercode/Application/database.py file.
# Create a get_db() function to yield the database using the session

def get_db():
  db = SessionLocal()
  try:
      yield db
  finally:
      db.close()

# This method will get the database and fetch the records from the database using the get_users() function in the /usercode/Application/crud.py file.
@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users 

# file to get the results from the above method.

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
    
# to get the results from the above method.

@app.get("/users/email/{user_email}", response_model=schemas.User)
def read_user_by_email(user_email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email = user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
    
# Create a new endpoint in the /usercode/Application/main.py file that accepts the user and gets the results from the above method.

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

# Create a new endpoint in the /usercode/Application/main.py file that accepts the user, checks if the user is available, and passes it to the above method to update the user.

@app.put("/users/", response_model=schemas.User)
def update_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        return crud.update_user(db=db, user=user)
    raise HTTPException(status_code=400, detail="User not Found")

# Create a new endpoint in the /usercode/Application/main.py file that accepts the user_id and passes it to the above method to delete the user.

@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user