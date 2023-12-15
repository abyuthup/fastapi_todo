from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URI = 'sqlite:///todosapp.db'

# test123#
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/TodoApplicationDatabase'
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:test123#@localhost:5432/TodoApplicationDatabase'

#mysql 
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1425mysql#@127.0.0.1:3306/TodoApplicationDatabase'


# engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={'check_same_thread': False}) # for sqlite3
engine = create_engine(SQLALCHEMY_DATABASE_URI) # for postgresql and mysql

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()