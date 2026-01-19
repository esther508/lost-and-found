from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


URL_DATABASE = 'mysql+pymysql://root:@localhost:3306/lostandfoundapplication'
# create sqlite engine instance
engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
