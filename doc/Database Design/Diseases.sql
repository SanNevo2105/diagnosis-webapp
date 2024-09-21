-- use team059;

-- create table disease_precaution(
-- 	name VARCHAR(50) primary key,
--     precaution_1 VARCHAR(50),
--     precaution_2 VARCHAR(50),
--     precaution_3 VARCHAR(50),
--     precaution_4 VARCHAR(50));

-- create table disease_description(
-- 	name VARCHAR(50) primary key,
--     description VARCHAR(400));
--     
-- create table Diseases(
-- 	name VARCHAR(50) primary key,
--     description VARCHAR(400),
--     precaution_1 VARCHAR(50),
--     precaution_2 VARCHAR(50),
--     precaution_3 VARCHAR(50),
--     precaution_4 VARCHAR(50));
--     
-- insert into Diseases select * from disease_description natural join disease_precaution;

-- delete from Diseases where name = 'Disease';

select * from Diseases;