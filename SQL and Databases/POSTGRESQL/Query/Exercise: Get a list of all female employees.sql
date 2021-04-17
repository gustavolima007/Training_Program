-- Exercise: Get a list of all female employees
SELECT
  first_name
FROM
  employees
WHERE gender = 'F';

-- OR
-- SELECT
--   *
-- FROM
--   employees
-- WHERE gender = 'F' ;