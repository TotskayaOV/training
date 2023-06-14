
-- Написать скрипт, возвращающий список имен (только firstname) пользователей без повторений в алфавитном порядке. [ORDER BY]
SELECT DISTINCT firstname FROM users ORDER BY firstname;


-- Выведите количество мужчин старше 35 лет [COUNT]
SELECT count(*) FROM profiles
WHERE (birthday + INTERVAL 35 YEAR) > NOW()
AND gender = 'm'; 

-- Сколько заявок в друзья в каждом статусе? (таблица friend_requests) [GROUP BY]
SELECT status, count(*) AS count 
FROM friend_requests 
GROUP BY status;

-- Выведите номер пользователя, который отправил больше всех заявок в друзья (таблица friend_requests) [LIMIT].
SELECT initiator_user_id, COUNT(status) AS cnt 
FROM friend_requests
GROUP BY initiator_user_id
ORDER BY cnt DESC
LIMIT 1;

-- Выведите названия и номера групп, имена которых состоят из 5 символов [LIKE].
SELECT name FROM communities
WHERE name LIKE '_____';



