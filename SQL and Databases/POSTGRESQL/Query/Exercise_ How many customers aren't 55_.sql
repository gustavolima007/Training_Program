-- The NOT Keyword 

-- Exercise: How many customers aren't 55?

SELECT count(age) FROM customers
WHERE NOT age = '55';