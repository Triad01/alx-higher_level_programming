-- script lists cities of califonia that can be found in the database
USE hbtn_0d_usa;
SELECT id, name FROM states
WHERE name = "California"
ORDER BY id;
