-- script lists cities of califonia that can be found in the database
SELECT id, name FROM cities
WHERE state_id = (SELECT id from states WHERE name = "California")
ORDER BY id;
