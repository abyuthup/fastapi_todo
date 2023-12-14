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




postgress create table query
 ################################
DROP TABLE IF EXISTS users;

CREATE TABLE users (
	id SERIAL,
	email varchar(200) DEFAULT NULL,
	username varchar(45) DEFAULT NULL,
	first_name varchar(45) DEFAULT NULL,
	last_name varchar(45) DEFAULT NULL,
	hashed_password varchar(200) DEFAULT NULL,
	is_active boolean DEFAULT NULL,
	role varchar(45) DEFAULT NULL,
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS todos;

CREATE TABLE todos (
	id SERIAL,
	title varchar(200) DEFAULT NULL,
	description varchar(200) DEFAULT NULL,
	priority integer DEFAULT NULL,
	complete boolean DEFAULT NULL,
	owner_id integer DEFAULT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (owner_id) REFERENCES users(id)
);

##############################################
