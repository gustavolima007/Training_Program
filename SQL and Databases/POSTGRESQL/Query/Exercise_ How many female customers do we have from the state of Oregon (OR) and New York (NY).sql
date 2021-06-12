-- Exercise: How many female customers do we have from the state of Oregon (OR) and New York (NY)

SELECT * FROM customers
WHERE (state = 'OR' OR state = 'NY') AND gender = 'F'


-- USE THIS QUERY BELLOW TO FIND HOW MANY FEMALE HAS

-- select count(firstname) from customers
-- where (state = 'NY' or state = 'OR') and gender = 'F'

-- RESULT: 200