-- number of recond with same value
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
