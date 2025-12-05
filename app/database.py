from datetime import time
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
#SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address>/hostname/<database_name>'
#SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:123456@localhost/fastapi'
SQLALCHEMY_DATABASE_URL ="postgresql://admin:xhy3ajG8gGRqRjkgy6pr6wQTHmUc5zqZ@dpg-d4ovouvgi27c73edo9og-a.oregon-postgres.render.com/fastapi_11ap"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


