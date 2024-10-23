CREATE DATABASE practical2;
USE practical2;

CREATE TABLE aids (
roll INT PRIMARY KEY,
Sname VARCHAR(50),
section varchar(5)
);

INSERT INTO aids
VALUES
(42, "Harshal", "A"),
(12, "Aditya", "B"),
(21, "Ganesh", "A"),
(41, "Suraj", "B");

CREATE TABLE aisa (
roll INT PRIMARY KEY,
Stname VARCHAR(50),
committee varchar(20),
paidmoney INT
);

INSERT INTO aisa
VALUES
(42, "Harshal", "utsah", 200),
(16, "Vedpathak", "uddan", 50),
(37, "shreyas", "utsah", 100),
(41, "Suraj", "datatak", 250);

-- Inner Join
SELECT * FROM aids
INNER JOIN aisa
ON aids.roll = aisa.roll;

-- Left Join
SELECT * FROM aids
LEFT JOIN aisa
ON aids.roll = aisa.roll;

-- Right Join
SELECT * FROM aids
RIGHT JOIN aisa
ON aids.roll = aisa.roll;

-- Full Join
SELECT * FROM aids
LEFT JOIN aisa
ON aids.roll = aisa.roll
UNION
SELECT * FROM aids
RIGHT JOIN aisa
ON aids.roll = aisa.roll;

-- Sub-Query
SELECT * FROM aisa
WHERE paidmoney > (SELECT AVG(paidmoney) FROM aisa);

-- Create a view
CREATE VIEW sampleview AS
SELECT * FROM aids;

SELECT * FROM sampleview;
