# for mysql
pip install pymysql

# connect app to db
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1425mysql#@127.0.0.1:3306/TodoApplicationDatabase'

# mysql create table query
 ################################
DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(200) DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `hashed_password` varchar(200) DEFAULT NULL,
  `is_active` int(1) DEFAULT NULL,
  `role` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `todos`;

CREATE TABLE `todos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `priority` int(1) DEFAULT NULL,
  `completed` int(1) DEFAULT NULL,
  `owner_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`owner_id`) REFERENCES users(`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

##############################################


# change postgres password

psql -h localhost -U postgres -d TodoApplicationDatabase
ALTER USER postgres PASSWORD 'new_password';
# quit
\q
