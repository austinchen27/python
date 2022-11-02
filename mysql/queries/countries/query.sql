-- QUERY 1 --
SELECT * FROM languages
WHERE language LIKE "Slovene"


-- QUERY 2 --
SELECT countries.name AS countries, COUNT(*) AS cities FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY COUNT(*) DESC


-- QUERY 3 --
SELECT cities.name, cities.population FROM cities
WHERE country_id = 136 AND population > 500000
ORDER BY population DESC


-- QUERY 4 --
SELECT languages.percentage FROM languages
WHERE percentage > 89
ORDER BY percentage DESC


-- QUERY 5 --
SELECT * FROM countries
WHERE surface_area < 501 AND population > 100000


-- QUERY 6 --
SELECT * FROM countries
WHERE government_form = "constitutional monarchy"
AND capital > 200
AND life_expectancy > 75


-- QUERY 7 --
SELECT countries.name, cities.name, cities.population, district FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE cities.population > 500000 AND district = "Buenos Aires" AND countries.name = "Argentina";

-- QUERY 8 --
SELECT countries.region, COUNT(*) AS countries FROM countries
GROUP BY region
ORDER BY COUNT(*) DESC





