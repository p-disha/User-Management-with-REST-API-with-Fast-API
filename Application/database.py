from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Specify the path for SQLAlchemy to store the database.
# Create a starting point for the database by creating an engine. This engine will be used to manage the connections with the database.
# Create a session controller to communicate with the database, and bind it with the engine from the previous step.
# Create a new base to create schemas.


SQLALCHEMY_DATABASE_URL = "sqlite:///sql_app.db"
engine= create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base=declarative_base()