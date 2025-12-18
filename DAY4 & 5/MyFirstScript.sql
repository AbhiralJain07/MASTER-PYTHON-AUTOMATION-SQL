CREATE DATABASE startsql;

USE startsql;

CREATE TABLE users(
id int AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
gender ENUM('Male' , 'female ' , 'other'),
date_of_birth DATE,
created_at TIMESTAMP DEFAULT current_timestamp
);

SELECT * FROM users;


-- delete the database
-- DROP DATABASE startsql;

-- rename the table 
-- RENAME TABLE USERS TO PROGRAMMERS
-- RENAME TABLE PROGRAMMERS TO USERS 