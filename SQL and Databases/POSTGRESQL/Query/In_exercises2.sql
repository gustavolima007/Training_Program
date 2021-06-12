-- * Question: How many cities are in the district of Zuid-Holland, Noord-Brabant and Utrecht?


SELECT count(NAME) FROM city
WHERE district IN ('Zuid-Holland', 'Noord-Brabant', 'Utrecht');

-- Result: There has 12 cities