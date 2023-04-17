-- Exercise 1: DVD Rental
-- Instructions

--     You were hired to babysit your cousin and you want to find a few movies that he can watch with you.
--         Find out how many films there are for each rating.

--         Get a list of all the movies that have a rating of G or PG-13.
--             Filter this list further: look for only movies that are under 2 hours long, and whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.

--         Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.
--         Now find the customer’s address, and use UPDATE to change the address to your address (or make one up).

SELECT rating , COUNT(*) FROM film GROUP BY rating;

SELECT * FROM film WHERE  (rating = 'G' or rating = 'PG-13') and length < 120 and rental_rate < 3.00 ORDER BY title;


UPDATE customer

SET first_name = 'Dekel', last_name='Matslich' , email = 'dekelmaz09@gmail.com' 

WHERE customer_id = 1










-- Exercise 2: students table
-- Instructions

-- Continuation of the Day1 Exercise XPGold : students table


-- Update

--     ‘Lea Benichou’ and ‘Marc Benichou’ are twins, they should have the same birth_dates. Update both their birth_dates to 02/11/1998.
--     Change the last_name of David from ‘Grez’ to ‘Guez’.


-- Delete

--     Delete the student named ‘Lea Benichou’ from the table.


-- Count

--     Count how many students are in the table.
--     Count how many students were born after 1/01/2000.

-- Insert / Alter

--     Add a column to the student table called math_grade.
--     Add 80 to the student which id is 1.
--     Add 90 to the students which have ids of 2 or 4.
--     Add 40 to the student which id is 6.
--     Count how many students have a grade bigger than 83
--     Add another student named ‘Omer Simpson’ with the same birth_date as the one already in the table. Give him a grade of 70.
--     Now, in the table, ‘Omer Simpson’ should appear twice. It’s the same student, although he received 2 different grades because he retook the math exam.
--     Bonus: Count how many grades each student has.
--         Tip: You should display the first_name, last_name and the number of grades of each student. If you followed the instructions above correctly, all the students should have 1 math grade, except Omer Simpson which has 2.
--         Tip : Use an alias called total_grade to fetch the grades.
--         Hint : Use GROUP BY.

-- SUM

--     Find the sum of all the students grades.



CREATE TABLE students(id serial primary key, last_name varChar , first_name varChar, birth_date date);

INSERT INTO students(first_name,last_name,birth_date) VALUES
('Marc','Benichou','1998-11-02'),
('Yoan','Cohen','2010-12-03'),
('Lea','Benichou','1987-07-27'),
('Amelia','Dux','1996-04-07'),
('David','Grez','2003-06-14'),
('Omer','Simpson','1980-10-03');

UPDATE students SET birth_date = '1998-11-02' WHERE last_name = 'Benichou';
UPDATE students SET last_name = 'Guez' WHERE first_name = 'David';
DELETE FROM students WHERE first_name = 'Lea';
SELECT COUNT(*) FROM students;
SELECT COUNT(*) FROM students WHERE birth_date > '2000-01-01';
ALTER TABLE students ADD COLUMN math_grade int;
UPDATE students SET math_grade = 80 WHERE id = 1;
UPDATE students SET math_grade = 90 WHERE id = 2 or id = 4;
UPDATE students SET math_grade = 40 WHERE id = 6;
SELECT COUNT(*) FROM students WHERE math_grade > 83;
INSERT INTO students(first_name,last_name,birth_date,math_grade) VALUES ('Omer','Simpson',(SELECT birth_date FROM students WHERE first_name = 'Omer'),70);
SELECT COUNT(*) as total_grades, first_name, last_name FROM students GROUP BY first_name , last_name
SELECT SUM(math_grade) from students;















-- Exercise 3 : Items and customers
-- Instructions

-- We will work on the public database that we created yesterday.

-- Part I

--     Create a table named purchases. It should have 3 columns :
--         id : the primary key of the table
--         customer_id : this column references the table customers
--         item_id : this column references the table items
--         quantity_purchased : this column is the quantity of items purchased by a certain customer\


-- Insert purchases for the customers, use subqueries:

--     Scott Scott bought one fan
--     Melanie Johnson bought ten large desks
--     Greg Jones bougth two small desks
-- The table purchases should look like this:
-- id 	customer_id 	item_id 	quantity_purchased
-- 1 	3 	3 	1
-- 2 	5 	2 	10
-- 3 	1 	1 	2

-- Part II

--     Use SQL to get the following from the database:
--         All purchases. Is this information useful to us?
--         All purchases, joining with the customers table.
--         Purchases of the customer with the ID equal to 5.
--         Purchases for a large desk AND a small desk

--     Use SQL to show all the customers who have made a purchase. Show the following fields/columns:
--         Customer first name
--         Customer last name
--         Item name

--     Add a row which references a customer by ID, but does not reference an item by ID (leave it blank). Does this work? Why/why not?


CREATE TABLE purchases(id serial primary key, customer_id int references customers(id), item_id int references items(id),quantity_purchased int);
INSERT INTO purchases(customer_id,item_id,quantity_purchased) VALUES (3 , 3 , 1) , (5 , 2 , 10) , (1 , 1 , 2);
SELECT * FROM purchases;
SELECT * FROM purchases JOIN customers ON purchases.customer_id = customers.id;
SELECT * FROM purchases JOIN customers ON purchases.customer_id = customers.id WHERE customer_id = 5;
SELECT * FROM purchases JOIN customers ON purchases.customer_id = customers.id WHERE item_id = (SELECT id from items WHERE item_name='Large Desk') OR item_id = (SELECT id from items WHERE item_name='Small Desk');
SELECT first_name , surname , item_name FROM purchases JOIN customers ON purchases.customer_id = customers.id JOIN items ON purchases.item_id = items.id;
INSERT INTO purchases(customer_id,quantity_purchased) VALUES (1 , 99); -- It worked, Because there is no constraint that says the value cant be a null value.



