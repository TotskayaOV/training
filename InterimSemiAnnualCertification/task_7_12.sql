DROP DATABASE IF EXISTS animal_nursery;
CREATE DATABASE IF NOT EXISTS animal_nursery;
USE animal_nursery;


CREATE TABLE `animals` (
  `id_type` INT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
  `type_animal` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_type`));
 

CREATE TABLE `pack_animals` (
  `id_genus` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `animal_genus` VARCHAR(45) NOT NULL,
  `type_id` INT UNSIGNED NOT NULL,
 	FOREIGN KEY (type_id) REFERENCES animals(id_type));


CREATE TABLE `pet_animals` (
  `id_genus` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `animal_genus` VARCHAR(45) NOT NULL,
  `type_id` INT UNSIGNED NOT NULL,
 	FOREIGN KEY (type_id) REFERENCES animals(id_type));
 

CREATE TABLE `horses` (
  `id_animal` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name_animal` VARCHAR(45) NOT NULL, 
  `birthday` DATE,
  `commands` TEXT,
  `genus_id` INT NOT NULL,
 	FOREIGN KEY (genus_id) REFERENCES pack_animals(id_genus));
 

CREATE TABLE `camels` (
  `id_animal` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name_animal` VARCHAR(45) NOT NULL, 
  `birthday` DATE,
  `commands` TEXT,
  `genus_id` INT NOT NULL,
 	FOREIGN KEY (genus_id) REFERENCES pack_animals(id_genus));
 

CREATE TABLE `donkeys` (
  `id_animal` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name_animal` VARCHAR(45) NOT NULL, 
  `birthday` DATE,
  `commands` TEXT,
  `genus_id` INT NOT NULL,
 	FOREIGN KEY (genus_id) REFERENCES pack_animals(id_genus));
 

CREATE TABLE `dogs` (
  `id_animal` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name_animal` VARCHAR(45) NOT NULL, 
  `birthday` DATE,
  `commands` TEXT,
  `genus_id` INT NOT NULL,
 	FOREIGN KEY (genus_id) REFERENCES pet_animals(id_genus));
 

CREATE TABLE `cats` (
  `id_animal` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name_animal` VARCHAR(45) NOT NULL, 
  `birthday` DATE,
  `commands` TEXT,
  `genus_id` INT NOT NULL,
 	FOREIGN KEY (genus_id) REFERENCES pet_animals(id_genus));
 

CREATE TABLE `hamsters` (
  `id_animal` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name_animal` VARCHAR(45) NOT NULL, 
  `birthday` DATE,
  `commands` TEXT,
  `genus_id` INT NOT NULL,
 	FOREIGN KEY (genus_id) REFERENCES pet_animals(id_genus));
 
INSERT INTO `animals` (`type_animal`) VALUES
('pack'), ('pet');

INSERT INTO `pack_animals` (`animal_genus`,`type_id`) VALUES
('horses', 1), ('camels', 1), ('donkeys', 1);

INSERT INTO `pet_animals` (`animal_genus`,`type_id`) VALUES
('dogs', 2), ('cats', 2), ('hamsters', 2);  

INSERT INTO `horses` (`name_animal`, `birthday`, `commands`, `genus_id`) VALUES
('Герцог', '2018-09-25', 'Ап', 1),
('Мальвина', '2021-03-08', 'Ап', 1),
('Черныш', '2015-11-18', 'Ап', 1),
('Индеец', '2015-11-18', null, 1);

INSERT INTO `camels` (`name_animal`, `birthday`, `commands`, `genus_id`) VALUES
('Адмирал', '2018-02-20', 'Вниз', 2),
('Белянин', '2021-03-08', 'Вниз', 2),
('Моргенштерн', '2022-11-08', 'Фу', 2);

INSERT INTO `donkeys` (`name_animal`, `birthday`, `commands`, `genus_id`) VALUES
('Шрек', '2020-05-10', null, 3),
('Катерина', '2019-01-22', null, 3),
('Барон', '2015-10-18', null, 3);

INSERT INTO `dogs` (`name_animal`, `birthday`, `commands`, `genus_id`) VALUES
('Шарик', '2018-04-10', 'Голос', 1),
('Белоснежка', '2023-01-12', 'Фу', 1),
('Бродяга', '2015-10-18', 'Сидеть', 1),
('Лайка', '2022-03-28', 'Лапу', 1);

INSERT INTO `cats` (`name_animal`, `birthday`, `commands`, `genus_id`) VALUES
('Маркиза', '2012-05-10', 'Кушать', 2),
('Стич', '2016-11-12', 'Кушать', 2),
('Фенек', '2018-10-03', 'Кушать', 2),
('Горлум', '2021-09-18', 'Кушать', 2);

INSERT INTO `hamsters` (`name_animal`, `birthday`, `commands`, `genus_id`) VALUES
('Пиня', '2022-03-12', null, 3),
('Кнопка', '2021-11-12', null, 3),
('Толстой', '2023-03-03', null, 3);

DROP TABLE camels;


CREATE TABLE horses_donkeys AS 
SELECT * FROM horses 
UNION 
SELECT * FROM donkeys;


CREATE TABLE young_animals AS
SELECT id_animal, name_animal, TIMESTAMPDIFF(MONTH, birthday, CURDATE()) AS age_in_months
	FROM 
	  (SELECT id_animal, name_animal, birthday
	  FROM dogs
	  WHERE TIMESTAMPDIFF(MONTH, birthday, CURDATE()) > 12 
	  	AND TIMESTAMPDIFF(MONTH, birthday, CURDATE()) < 36
	  UNION
	  SELECT id_animal, name_animal, birthday
	  FROM cats
	  WHERE TIMESTAMPDIFF(MONTH, birthday, CURDATE()) > 12 
	  	AND TIMESTAMPDIFF(MONTH, birthday, CURDATE()) < 36
	  UNION
	  SELECT id_animal, name_animal, birthday
	  FROM hamsters
	  WHERE TIMESTAMPDIFF(MONTH, birthday, CURDATE()) > 12 
	  	AND TIMESTAMPDIFF(MONTH, birthday, CURDATE()) < 36
	  UNION
	  SELECT id_animal, name_animal, birthday
	  FROM horses_donkeys
	  WHERE TIMESTAMPDIFF(MONTH, birthday, CURDATE()) > 12 
	  	AND TIMESTAMPDIFF(MONTH, birthday, CURDATE()) < 36) 
	 AS subquery;
	
	
	 
CREATE TABLE all_animals AS
SELECT * FROM 
	horses_donkeys h JOIN (SELECT * FROM pack_animals p JOIN animals a ON p.type_id=a.id_type) i
	ON h.genus_id=i.id_genus
UNION ALL 
SELECT * FROM 
	dogs d JOIN (SELECT * FROM pet_animals p JOIN animals a ON p.type_id=a.id_type) i
	ON d.genus_id=i.id_genus
UNION ALL 
SELECT * FROM 
	cats c JOIN (SELECT * FROM pet_animals p JOIN animals a ON p.type_id=a.id_type) i
	ON c.genus_id=i.id_genus
UNION ALL 
SELECT * FROM 
	hamsters hm JOIN (SELECT * FROM pet_animals p JOIN animals a ON p.type_id=a.id_type) i
	ON hm.genus_id=i.id_genus;