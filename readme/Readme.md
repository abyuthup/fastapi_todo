# FastAPI Application

This is a simple FastAPI application.



Create virtual environment
python -m venv fastapienv

# Activate venv
source fastapienv/bin/activate


## Installation

pip install fastapi
pip install "uvicorn[standard]"

//install database
pip install sqlalchemy
# install passlib
pip install "passlib[bcrypt]"
# to work with form data and file uploading we need multipart lib.
pip install python-multipart
# for jwt 
pip install "python-jose[cryptography]"
# for postgresql
pip install psycopg2-binary
# for mysql
pip install pymysql
# for alembic
pip install alembic


## Run uvicorn server
uvicorn main:app --reload



## connect database with sqlite3
sqlite3 todos.db

# change show mode to box
.mode box


# select interpreter
fastapienv/bin/python3.11




# show db schema
.schema

# insert values
insert into todos (title,description, priority,completed) values ('go to stores','pick up eggs',5,False);

# quit
.quit


#for random unique string key for jwt secret
openssl rand -hex 32





