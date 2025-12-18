USE startsql;
DROP TABLE IF EXISTS addresses;

CREATE TABLE addresses (
id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT,
street VARCHAR(255),
city VARCHAR(100),
state VARCHAR(100),
pincode VARCHAR(10),
CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

INSERT INTO addresses (user_id, street, city, state, pincode)
VALUES
(41, '221B MG Road', 'Mumbai', 'Maharashtra', '400001'),
(42, '14 Park Street', 'Kolkata', 'West Bengal', '700016'),
(43, '32 Residency Road', 'Bengaluru', 'Karnataka', '560025'),
(44, '5 North Usman Road', 'Chennai', 'Tamil Nadu', '600017'), 
(45, '17 Hazratganj', 'Lucknow', 'Uttar Pradesh', '226001'),
(46, '55 Banjara Hills', 'Hyderabad', 'Telangana', '500034'),
(47, '88 Connaught Place', 'Delhi', 'Delhi', '110001'),
(48, '10 MG Marg', 'Dehradun', 'Uttarakhand', '248001'),
(49, '23 Brigade Road', 'Bengaluru', 'Karnataka', '560025'),
(50, '45 Marine Drive', 'Mumbai', 'Maharashtra', '400020'),
(51, '67 Ashoka Road', 'Delhi', 'Delhi', '110001'),
(52, '89 MG Road', 'Pune', 'Maharashtra', '411001'),
(53, '12 Brigade Road', 'Bengaluru', 'Karnataka', '560025'),
(54, '34 Park Street', 'Kolkata', 'West Bengal', '700016'),
(55, '56 Connaught Place', 'Delhi', 'Delhi', '110001');

