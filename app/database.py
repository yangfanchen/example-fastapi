from datetime import time
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
#SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address>/hostname/<database_name>'
#SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:123456@localhost/fastapi'
#SQLALCHEMY_DATABASE_URL ="postgresql://admin:xhy3ajG8gGRqRjkgy6pr6wQTHmUc5zqZ@dpg-d4ovouvgi27c73edo9og-a.oregon-postgres.render.com/fastapi_11ap"
#postgresql://admin:jjOEwz9xHW1HGol4WOmi2W93ngTBedIR@dpg-d4qdbebe5dus73elnni0-a.virginia-postgres.render.com/fastapi_o5ta
SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg2://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

#SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:password123@postgres:5432/fastapi"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


