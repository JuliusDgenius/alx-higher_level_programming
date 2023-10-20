-- list all records excepts records without name value.
SELECT score, name
FROM second_table
WHERE name != ''
ORDER BY score DESC;
