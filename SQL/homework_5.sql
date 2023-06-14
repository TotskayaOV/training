-- Создайте представление с произвольным SELECT-запросом из прошлых уроков [CREATE VIEW]
-- "Подсчитать количество групп (сообществ), в которые вступил каждый пользователь."
USE vk;

CREATE VIEW users_community AS
SELECT user_id, COUNT(community_id)
FROM users_communities
GROUP BY user_id;


-- Выведите данные, используя написанное представление [SELECT]

SELECT * FROM users_community


-- Удалите представление [DROP VIEW]

DROP VIEW users_community 

-- * Сколько новостей (записей в таблице media) у каждого пользователя? 
-- Вывести поля: news_count (количество новостей), user_id (номер пользователя), user_email (email пользователя). 
-- Попробовать решить с помощью CTE или с помощью обычного JOIN.

SELECT COUNT(media.body) AS news_count, media.user_id, users.email AS user_email
FROM media JOIN users ON media.user_id = users.id 
GROUP BY user_id

WITH cte AS (
	SELECT COUNT(*) as news_count, user_id 
	FROM media 
	GROUP BY user_id
)
SELECT 
	news_count,	user_id, email AS user_email
FROM cte
JOIN users on users.id = cte.user_id;