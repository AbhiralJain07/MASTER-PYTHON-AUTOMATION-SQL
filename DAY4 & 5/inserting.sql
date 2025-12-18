USE startsql;

-- INSERT WITHOUT SPECIFYING COLUMNS
-- INSERT INTO users VALUES (10 ,'alEce@gmail.com', "AlICE", "Female" ,"1999-12-18", DEFAULT );
-- SELECT * FROM USERS;

-- INSERT WITH SPECIFYING COLUMNS
INSERT INTO users (name ,email, gender, date_of_birth) VALUES
('Harry' ,'harry@gmail.com' , 'Male', '2000-12-28' ),
('Bob' , 'bob@gmail.com' , 'Female' , '2000-07-20'),
('Hari' , 'hari@gmail.com' , 'Male' , '2003-07-19'),
('Bikas' , 'bikas@gmail.com' , 'Female' , '1999-01-02'),
('Prahlad' , 'prahlad@gmail.com' , 'Male' , '1998-03-30'),
('risi' , 'risi@gmail.com' , 'Female' , '2006-07-20');
SELECT * FROM USERS;