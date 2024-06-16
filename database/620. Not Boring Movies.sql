-- https://leetcode.com/problems/not-boring-movies/
SELECT *
FROM cinema
WHERE cinema.description != 'boring' and (id & 1) = 1
ORDER BY rating DESC 