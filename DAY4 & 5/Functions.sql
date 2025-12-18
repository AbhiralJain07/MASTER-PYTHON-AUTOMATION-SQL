USE startsql;

SELECT * FROM users;
-- SELECT COUNT(*) FROM users;
-- SELECT COUNT(*) FROM users WHERE gender = 'female';
-- SELECT MIN(date_of_birth) AS min_age, MAX(date_of_birth) AS max_age FROM users;
-- SELECT gender, AVG(date_of_birtjh) AS avg_age  FROM users GROUP BY gender ;`
SELECT id , gender, name , length(name) AS name_len FROM users;
SELECT id , gender, lower( name ) as lower, concat(LOWER(name),  "5677") as username   , length(name) AS name_len FROM users; 
SELECT id , gender, lower( name ) as lower, concat(LOWER(name),  "5677") as username,NOW() as time, length(name) AS name_len FROM users; 
SELECT id , gender, lower( name ) as lower, concat(LOWER(name),  "5677") as username, YEAR() as time, length(name) AS name_len FROM users; 
SELECT id , gender, lower( name ) as lower, concat(LOWER(name),  "5677") as username, YEAR(date_of_birth) as yob  , length(name) AS name_len FROM users; 
SELECT name , DATEDIFF(CURDATE(), date_of_birth) AS DAYS FROM users;