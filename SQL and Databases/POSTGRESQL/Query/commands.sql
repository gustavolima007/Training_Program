-- POSTGRES DATABASE

-- To select a column

SELECT * FROM departments;

-- To change localhost postgres password in linux terminal:

ALTER USER postgres PASSWORD 'root';

-- Selecting and rename columns:

SELECT emp_no as "Employees Number" from employees;

-- Other example

SELECT emp_no as "Employees Number", birth_date as "Birthday", first_name as "First Name" from employees

-- Column Concatenation

SELECT emp_no, concat(first_name, ' ', last_name) as "Employee Name" from employees
