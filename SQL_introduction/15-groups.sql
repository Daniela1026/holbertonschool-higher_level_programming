-- the number of records for this score with the label number
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score DESC;