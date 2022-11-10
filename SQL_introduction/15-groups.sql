-- the number of records for this score with the label number
SELECT score, COUNT('score') as number
FROM second_table
GROUP BY score
ORDER BY score DESC;