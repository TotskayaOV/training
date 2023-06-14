DROP TABLE IF EXISTS user_wall;
CREATE TABLE user_wall (
	id SERIAL, -- SERIAL = BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE
	user_id BIGINT UNSIGNED NOT NULL,
    body TEXT,
    created_at DATETIME DEFAULT NOW(),
    `comment_status` ENUM ('activ', 'inactiv'),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS comment_wall;
CREATE TABLE message_wall (
	id SERIAL,
	wall_id BIGINT UNSIGNED NOT NULL,
	user_id BIGINT UNSIGNED NOT NULL,
	commenting_user_id BIGINT UNSIGNED NOT NULL,
    body TEXT,
    created_at DATETIME DEFAULT NOW(),
    
    FOREIGN KEY (wall_id) REFERENCES user_wall(id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (commenting_user_id) REFERENCES users(id)
);

INSERT INTO users (firstname, lastname, email, phone) VALUES
('Иван', 'Соколов', 'ivsokol@mail.ru', 79239721902),
('Майя', 'Швах', 'scheinen@gmail.com', 79748229012),
('Палое', 'Вильямс', 'paloe234@yahoo.com', 12349870123),
('Егор', 'Прилепин', 'bigman@ya.ru', 79130010102),
('Маша', 'Ненашева', 'masha2020@mail.ru', 79529104792),
('Илья', 'Иванов', 'ilia.ivanov@gmail.com', 79139731902),
('Илья', 'Сибирцев', 'sibircev11@gmail.com', 795082212792),
('Анна', 'Дягилева', 'diagil.anna@gmail.com', 79230086724),
('Стас', 'Марков', 'markusha@ya.ru', 79035011152),
('Тифон', 'Петров', 'tifon23@narod.ru', 79139104756);

/*
 Чтобы выполнить задачу со звездочкой нужно было заполнить поля профиля, 
 поэтому пришлось заполнять таблицу медиа в урезанном варианте
 */

INSERT INTO media_types  (name) VALUES ('jpg'), ('png');

INSERT INTO media (media_type_id, user_id, filename) VALUES
(1, 1, 'image_2023-05-03_18-36-22'),
(1, 2,'IMG_0074'),
(2, 3, '914d45b3e7d143c4a145c32b8341eb2f'),
(1, 4, 'image_2023-01-13'),
(1, 5, 'IMG_0074'),
(1, 6, 'image (5)'),
(1, 7, 'image'),
(2, 8, '23.02.2023 коор'),
(2, 9, 'photo_2023-02-14_00-33-49'),
(2, 10, 'photo_2020-12-20');

/*
 заполнение профилей пользователей
 */

INSERT INTO profiles (user_id, gender, birthday, photo_id, hometown) VALUES
(1, 'M', DATE('2000-01-17'), 1, 'Москва'),
(2, 'F', DATE('1990-05-07'), 2, 'Санкт-Петербург'),
(3, 'M', DATE('1984-11-17'), 3, 'Drezden'),
(4, 'M', DATE('2005-01-11'), 4, 'Москва'),
(5, 'F', DATE('2008-04-23'), 5, 'Петропавловск'),
(6, 'M', DATE('2001-02-19'), 6, 'Муромск'),
(7, 'M', DATE('2000-07-28'), 7, 'Новосибирск'),
(8, 'F', DATE('2002-03-01'), 8, 'Дудинка'),
(9, 'M', DATE('2007-07-09'), 9, 'Москва'),
(10, 'M', DATE('2000-10-06'), 10, 'Санкт-Петербург');

ALTER TABLE profiles ADD COLUMN is_activ BOOLEAN NOT NULL DEFAULT FALSE;
UPDATE profiles SET is_activ=TRUE WHERE birthday>DATE('2005-05-24');

DELETE FROM messages WHERE created_at>NOW();