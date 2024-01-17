-- script lists all cities contained in the database
SELECT cities.id, cities.name
FROM cities
INNER JOIN states
ON cities.id = states.id
GROUP BY cities.id;
