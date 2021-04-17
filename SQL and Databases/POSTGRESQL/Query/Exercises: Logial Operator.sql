-- Exercises

-- Select people either under 30 or over 50 with an income above 50000 that are from either Japan or Australia

-- select * from customers
-- where (age < 30 or age >= 50) and income > 50000 and (country = 'Japan' or country = 'Australia')
 
--  Result: 868
 
-- What was our total sales in June of 2004 for orders over 100 dollars?

SELECT sum(totalamount) FROM orders
WHERE (orderdate > '2004-06-01' AND orderdate < '2004-06-30') AND totalamount > 100 

-- Result: 190.750,72