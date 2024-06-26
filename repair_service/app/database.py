from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings import settings

if (settings.postgres_url!='')
    engine = create_engine(settings.postgres_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()