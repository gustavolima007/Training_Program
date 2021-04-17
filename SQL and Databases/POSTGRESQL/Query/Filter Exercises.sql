-- How many female customers do we have from the state of Oregon (OR)?

-- select count(firstname) from customers
-- where state = 'OR' and gender = 'F'

-- Result: 106 

-- Who over the age of 44 has an income of 100 000 or more?

-- SELECT count(firstname) from customers
-- where age > 44 and income >= 100000
-- 
-- Result: 2497

-- Who between the ages of 30 and 50 has an income of less than 50 000?

-- select count(firstname) from customers
-- where income < 50000 and (age >= 30 and age <= 50) 
-- 
-- Result: 2362

-- What is the average income between the ages of 20 and 50?

-- select avg(income) from customers
-- where age > 20 and age < 50
-- 
-- Result: 59.409,92