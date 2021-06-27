/*
* DB: Employees
* Table: employees
* Question: Sort employees by first name ascending and last name descending
*/

--select * from employees
--order by first_name, last_name desc;

/*
* DB: Employees
* Table: employees
* Question: Sort employees by age
*/

--select * from employees
--order by birth_date;

/*
* DB: Employees
* Table: employees
* Question: Sort employees who's name starts with a "k" by hire_date
*/

SELECT * FROM employees
WHERE last_name ILIKE 'K%'
ORDER BY hire_date
