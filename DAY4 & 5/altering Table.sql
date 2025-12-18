-- ALTERING A TABLE


-- ALTER TABLE users ADD column is_active BOOLEAN DEFAULT true ; 
-- SELECT * from users;

-- ALTER TABLE users DROP column is_active;
-- SELECT * from users;


ALTER TABLE users MODIFY column email VARCHAR(100) AFTER id;
SELECT * from users;