-- In this exercise we will be using the actors table from todays lesson.
-- 1. Count how many actors are in the table.
-- 2. Try to add a new actor with some blank fields. What do you think the outcome will be ?






CREATE TABLE actors(id serial primary key , first_name varChar , last_name varChar , age date, number_oscars smallint);
INSERT INTO actors(first_name, last_name, age, number_oscars)
VALUES ('Angelina' , 'Jolie' , '1975-06-04' , 1),
('George' , 'Clooney' , '1961-06-05' , 2),
('Jennifer' , 'Aniston' , '1969-02-11' , 0),
('Matt' , 'Damon' , '1970-08-10' , 5);
SELECT COUNT(id) from actors;
INSERT INTO actors(first_name,last_name,age) VALUES ('MARK' , 'ROBER' , '1990-01-01');
SELECT * FROM actors;

-- Adds null to the table
