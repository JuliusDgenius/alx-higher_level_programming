-- Lists the number of records with the same score.
SELECT score FROM second_table COUNT(*) GROUP BY score
