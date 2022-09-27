-- In 6.sql, write a SQL query to determine the average rating of all movies released in 2012.

SELECT AVG(rating)
FROM ratings AS r, movies AS m
WHERE m.id = r.movie_id AND m.year = 2012;
