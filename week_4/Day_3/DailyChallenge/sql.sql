-- Instructions

-- You are going to practice tables relationships

-- Part I

--     Create 2 tables : Customer and Customer profile. They have a One to One relationship.
--         A customer can have only one profile, and a profile belongs to only one customer
--         The Customer table should have the columns : id, first_name, last_name NOT NULL
--         The Customer profile table should have the columns : id, isLoggedIn DEFAULT false (a Boolean), customer_id (a reference to the Customer table)

--     Insert those customers
--         John, Doe
--         Jerome, Lalu
--         Lea, Rive

--     Insert those customer profiles, use subqueries
--         John is loggedIn
--         Jerome is not logged in

-- Use the relevant types of Joins to display:

--     The first_name of the LoggedIn customers
--     All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
--     The number of customers that are not LoggedIn




-- Part II:

--  1.   Create a table named Book, with the columns : book_id SERIAL PRIMARY KEY, title NOT NULL, author NOT NULL

--  2. Insert those books :

--     Alice In Wonderland, Lewis Carroll
--     Harry Potter, J.K Rowling
--     To kill a mockingbird, Harper Lee

--  3. Create a table named Student, with the columns : student_id SERIAL PRIMARY KEY, name NOT NULL UNIQUE, age.
-- 	   Make sure that the age is never bigger than 15 (Find an SQL method);

--  4. Insert those students:

--     John, 12
--     Lera, 11
--     Patrick, 10
--     Bob, 14


-- 1
-- CREATE TABLE book(book_id serial primary key , title varChar NOT NULL , author varChar NOT NULL);

-- 2
-- INSERT INTO book(title , author) VALUES ('Alice In Wonderland','Lewis Carroll'),('Harry Potter','J.K Rowling'),('To Kill a mockingbird','Harper Lee');

--3
-- CREATE TABLE student(student_id SERIAL PRIMARY KEY, name varChar NOT NULL UNIQUE , age int check(age <= 15));

-- 4
-- INSERT INTO student(name,age) VALUES ('John',12),('Lera',11),('Patrick',10),('Bob',14);

--ANSWERS:
--Part 1

--1
-- CREATE TABLE customer (
-- id serial primary key,
-- first_name varChar,
-- last_name varChar not null);

--2
-- CREATE TABLE customer_profile (
-- id serial primary key,
-- isLoggedIn bool DEFAULT false,
-- customer_id int REFERENCES Customer(id));

--3
-- INSERT INTO Customer(first_name, last_name)
-- VALUES('John','Doe'),('Jerome', 'Lalu'), ('Lea', 'Rive');
-- INSERT INTO Customer_profile(isLoggedIn, customer_id)
-- VALUES(true, (SELECT id FROM customer WHERE first_name = 'John')),(false ,(SELECT id FROM customer WHERE first_name = 'Jerome'));

--4
-- SELECT first_name , isLoggedIn from customer LEFT JOIN customer_profile ON customer.id = customer_profile.customer_id; 
-- SELECT COUNT(*) from customer_profile WHERE isLoggedIn = false 

--Part 2

