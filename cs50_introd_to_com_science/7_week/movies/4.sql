-- In 4.sql, write a SQL query to determine the number of movies with an IMDb rating of 10.0.

SELECT count(*)
FROM movies AS m, ratings AS r
WHERE m.id = r.movie_id AND r.rating = '10.0';