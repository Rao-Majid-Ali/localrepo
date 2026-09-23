
CREATE DATABASE if not exists instagram;
use instagram;
create table user(
	id int primary key,
    Name varchar(30) not null,
    Age int ,
    Email varchar(50) unique,
    Followers int DEFAULT 0,
    Following int,
    CONSTRAINT age_check CHECK ( age >= 13)
);

INSERT INTO post
(Id,content,user_id)
VALUES
(101,"This is my pic",1),
(102,"This is how i know",5);

INSERT INTO user
(id,Name,Age,Email,Followers,Following)
VALUES
(8,"AHMAD",16,"ahmadali@gmail.com",110,150);

INSERT INTO user
(id,Name,Age,Email,Followers,Following)
VALUES
(1,"Majid",15,"majidali@gmail.com",110,150),
(2,"Manan",14,"manan@gmail.com",80,9),
(3,"Bilal",17,"bilal@gmail.com",107,10),
(4,"Abdullah",15,"abdullah@gmail.com",10,100);

create table post (
		Id int primary key,
        content varchar(100),
        user_id int,
        foreign key (user_id) references user(id)
);

SELECT * FROM user;
SELECT Name , Age , Email FROM user;
SELECT DISTINCT Age FROM user;
SELECT Name
FROM user
where followers >50;

SELECT Name,Age
FROM user
where Age+1 =15;

SELECT Name,Age,Followers
FROM user
where Age > 15 AND Followers >100;

SELECT Name,Age,Followers
FROM user
where Age > 15 or Followers >100;

SELECT Name,Age,Followers
FROM user
where Age between 14 and 17;

SELECT Name,Followers,Email
FROM user
where Email IN("majid@gmail.com","majidali@gmail.com","abcd@gmail.com","abdullah@gmail.com","bob@gmail.com");

SELECT Name,Followers,Email,Age
FROM user
where Age IN(14,19,20);

SELECT Name,Followers,Age
FROM user
where Age not IN(14,19,20);

SELECT Name,Followers,Age
FROM user
where Age > 13
limit 3;

SELECT Name,Followers,Age
FROM user
limit 2;

SELECT Name,Followers,Age
FROM user
ORDER BY Followers ASC;

SELECT Name,Followers,Age
FROM user
ORDER BY Followers DESC;

SELECT Name,Followers,Age
FROM user
ORDER BY Age,Followers ASC;

SELECT max(age)
FROM user;

SELECT MIN(age)
FROM user;

SELECT max(age)
FROM user;

SELECT COUNT(Name)
FROM user;

SELECT sum(age)
FROM user;

SELECT avg(Followers)
FROM user;

SELECT avg(Age)
FROM user;

SELECT age,count(id)
FROM user
GROUP BY Age;

SELECT age,max(Followers)
FROM user
GROUP BY Age
HAVING max(Followers) > 100
ORDER BY Age DESC;
 
 
UPDATE user
SET Followers = 600
where age = 15;

DELETE FROM user
WHERE age = 14;

ALTER TABLE user
ADD COLUMN City VARCHAR(30) DEFAULT "Lahore"; 

ALTER TABLE user
ADD COLUMN  Country VARCHAR(30) DEFAULT "Pakistan";

ALTER TABLE user
DROP COLUMN Country;

ALTER TABLE instauser
RENAME TO user;

ALTER TABLE user 
CHANGE COLUMN City cities varchar(20) DEFAULT "ISB";
 
ALTER TABLE user
MODIFY cities VARCHAR(20) DEFAULT "MULTAN";

TRUNCATE TABLE User 

select * from user;