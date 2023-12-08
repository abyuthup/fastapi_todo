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


## Run uvicorn server
uvicorn main:app --reload



## connect database with sqlite3
sqlite3 todos.db


# select interpreter
fastapienv/bin/python3.11


# show db schema
.schema

# insert values
insert into todos (title,description, priority,completed) values ('go to stores','pick up eggs',5,False);

# quit
.quit


