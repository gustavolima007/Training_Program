-- Using AND, OR

SELECT first_name, last_name, hire_date, gender, birth_date FROM employees
WHERE first_name = 'Georgi' AND last_name = 'Facello' 
OR first_name = 'Bezalel' AND last_name = 'Simmel'

