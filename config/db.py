from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:Sp5Qz2L077#0_4@localhost:3306/dbuaesp")

meta = MetaData()

SessionLocal = sessionmaker(autoflush=False, bind=engine )

conn = engine.connect()

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()