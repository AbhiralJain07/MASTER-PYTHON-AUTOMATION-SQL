USE startsql;

SELECT * from users WHERE gender != 'Male';
SELECT * from users WHERE date_of_birth <  '2000-01-01';
SELECT * from users WHERE id< 10;
SELECT * from users WHERE date_of_birth IS NOT NULL;
SELECT * from users WHERE date_of_birth IS NULL; 
SELECT * from users WHERE date_of_birth IS NOT NULL;
SELECT * from users WHERE date_of_birth between '1999-12-31' AND '2006-12-31';
SELECT * from users WHERE gender IN ('Male' , 'Other' );
SELECT * from users WHERE name LIKE 'A%';
SELECT * from users WHERE name LIKE '%a' ;
SELECT * from users WHERE name LIKE '%Li%' ;
SELECT * from users WHERE date_of_birth <  '2000-01-01' AND gender = 'female'; 
SELECT * from users WHERE date_of_birth <  '2000-01-01' OR gender = 'female'; 
SELECT * from users ORDER BY date_of_birth ASC;
SELECT * from users ORDER BY name DESC; 
SELECT * from users LIMIT 5; 
SELECT * from users ORDER BY created_at DESC LIMIT 10; 