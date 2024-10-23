CREATE DATABASE practical1;
USE practical1;

CREATE TABLE employees (
employee_id INT AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(50),
last_name VARCHAR(50),
hire_date DATE
);

CREATE TABLE orders (
order_id INT PRIMARY KEY,
customer_id INT,
order_date DATE,
total_amount DECIMAL(10, 2),
status VARCHAR(20)
);

CREATE VIEW employee_view AS
SELECT first_name, last_name
FROM employees
WHERE hire_date > '2022-01-01';

CREATE INDEX idx_employee_first_name ON employees(first_name);

ALTER TABLE employees
ADD CONSTRAINT UNIQUE (hire_date);

INSERT INTO employees (employee_id, first_name, last_name, hire_date)
VALUES (3, 'ITYA', 'JAHAV', '2023-01-25');

INSERT INTO employees (first_name, last_name, hire_date)
VALUES
('Mary', 'Johnson', '2023-02-28'),
('Robert', 'Williams', '2023-03-05'),
('Linda', 'Brown', '2023-03-10');

SELECT * FROM employees WHERE first_name = 'ADITYA';

SELECT first_name, last_name, hire_date
FROM employees
WHERE hire_date >= '2023-01-01'
ORDER BY hire_date DESC;

UPDATE employees
SET hire_date='2023-01-20'
WHERE employee_id=1;

DELETE FROM employees WHERE employee_id=3;

SELECT * FROM employees WHERE employee_id >= 2;

SELECT COUNT(*) FROM employees;

SELECT employee_id FROM employees WHERE last_name = 'BODAKHE'
UNION
SELECT first_name FROM employees WHERE last_name = 'BODAKHE';

SELECT employees.employee_id, employees.first_name, employees.last_name, orders.order_date
FROM employees
INNER JOIN orders ON employees.employee_id = orders.customer_id;
