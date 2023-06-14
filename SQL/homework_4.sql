-- Подсчитать количество групп (сообществ), в которые вступил каждый пользователь.
SELECT user_id, COUNT(community_id)
FROM users_communities
GROUP BY user_id;


-- Подсчитать количество пользователей в каждом сообществе.
SELECT name, count(user_id)
FROM communities JOIN users_communities ON communities.id = users_communities.community_id
GROUP BY name; 

-- Пусть задан некоторый пользователь. Из всех пользователей соц. сети найдите человека, который больше всех общался с выбранным пользователем (написал ему сообщений).

SELECT from_user_id
FROM messages JOIN users ON messages.to_user_id = users.id
WHERE messages.to_user_id = 1
GROUP BY from_user_id
ORDER BY count(to_user_id) DESC
LIMIT 1;

-- * Подсчитать общее количество лайков, которые получили пользователи младше 18 лет..
SELECT count(likes.user_id) AS count_messages
FROM likes 
JOIN users ON likes.user_id = users.id 
JOIN profiles ON users.id = profiles.user_id 
WHERE 
     TIMESTAMPDIFF(YEAR, birthday, NOW()) < 18; 

-- * Определить кто больше поставил лайков (всего): мужчины или женщины.
SELECT profiles.gender, count(likes.user_id) AS count_messages
FROM likes 
JOIN users ON likes.user_id = users.id 
JOIN profiles ON users.id = profiles.user_id 
GROUP BY profiles.gender
ORDER BY count_messages DESC;