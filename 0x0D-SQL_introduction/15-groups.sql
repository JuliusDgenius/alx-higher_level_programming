-- Lists the number of records with the same score.
SELECT score FROM second_table, COUNT(*) AS number
GROUP BY score
ORDER BY number DESC;
