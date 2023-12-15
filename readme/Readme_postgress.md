# for postgresql
pip install psycopg2-binary

# connect app to db
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:test123#@localhost:5432/TodoApplicationDatabase'

# postgress create table query
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
	completed boolean DEFAULT NULL,
	owner_id integer DEFAULT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (owner_id) REFERENCES users(id)
);

##############################################


# change postgres password

psql -h localhost -U postgres -d TodoApplicationDatabase
ALTER USER postgres PASSWORD 'new_password';
# quit
\q
