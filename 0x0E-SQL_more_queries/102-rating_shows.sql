-- Script to list all shows from hbtn_0d_tvshows_rate by their rating sum

SELECT title, SUM(rate) AS rating_sum
FROM tv_shows AS s
JOIN tv_show_ratings AS r
ON s.show_id = r.show_id
GROUP BY title
ORDER BY rating_sum DESC;

