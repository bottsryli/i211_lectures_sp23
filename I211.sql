CREATE TABLE customer
(
id INT(3),
fname VARCHAR(15),
lname VARCHAR(15),
gender CHAR(1),
phone CHAR(12)
) ENGINE=INNODB;

CREATE TABLE store
(
store_id INT(4),
open_date DATE,
city VARCHAR(20),
state CHAR(20),
addr_num VARCHAR(15),
addr_street VARCHAR(15),
zip INT(5),
open_time TIME,
close_time TIME
) ENGINE=INNODB;

CREATE TABLE pet
(
pet_id INT(4),
dob DATE,
name VARCHAR(15),
species VARCHAR(15),
breed VARCHAR(15),
gender CHAR(1),
price DECIMAL(5,2),
date_in DATE
) ENGINE=INNODB;

CREATE TABLE dinosaur
(
id INT NOT NULL,
slug VARCHAR(15),
name VARCHAR(20),
description TEXT,
image VARCHAR(25),
image_credit VARCHAR(60),
source_url VARCHAR(65),
source_credit VARCHAR(150)
) ENGINE=INNODB;



ALTER TABLE pet ADD n_date DATE;

ALTER TABLE customer DROP COLUMN lname;
ALTER TABLE customer DROP COLUMN fname;

ALTER TABLE customer ADD last_name VARCHAR(15);
ALTER TABLE customer ADD first_name VARCHAR(15);

ALTER TABLE store MODIFY addr_street VARCHAR(25);

INSERT INTO customer (id, first_name, last_name, gender, phone) VALUES
(101, 'Pat', 'Hammonds', 'F', '801-555-4360'),
(102, 'Chris', 'Fields', 'M', '312-633-0912'),
(103, 'Jordan', 'Vills', 'M', '535-741-2873'),
(104, 'Mary', 'Patrick', 'F', '940-324-8860'),
(105, 'Morgan', 'Knightly', 'M', '621-486-0213'),
(106, 'Blai', 'Woods', 'F', '591-204-7715'),
(107, 'Mason', 'Browning', 'M', '422-846-9091');

INSERT INTO pet (pet_id, dob, name, species, breed, gender, price, date_in, n_date) VALUES
(1001, "2021-05-20", "Gabby", "cat", "tabby", "F", 39.99, "2021-06-30", "2021-08-18"),
(1002, "2020-10-11", "Spot", "dog", "yorkie", "M", 499.99, "2020-12-01", "2023-12-01"),
(1003, "2021-05-02", "Khaleesi", "dog", "shepherd", "F", 599.99, "2021-06-15", "2021-11-06");


UPDATE customer SET phone="812-335-9075" WHERE last_name="Vills" AND first_name="Jordan";
-- or
UPDATE customer SET phone="812-335-9075" WHERE id=103;
--
UPDATE pet SET n_date="2023-02-02" WHERE name="Spot";

SELECT name,breed,price
FROM pet WHERE species="dog";

SELECT phone FROM customer
WHERE last_name="Hammonds" AND first_name="Pat";

SELECT name FROM pet WHERE dob,"2022-01-01";

DELETE FROM pet WHERE name="Spot";

DELETE FROM customer WHERE last_name="Fields" AND first_name="Chris";

SELECT * FROM pet

SELECT name, dob
FROM pet
WHERE species='dog' AND n_date IS NULL;