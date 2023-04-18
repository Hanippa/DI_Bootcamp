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


--  5. Create a table named Library, with the columns :

--     book_fk_id ON DELETE CASCADE ON UPDATE CASCADE
--     student_id ON DELETE CASCADE ON UPDATE CASCADE
--     borrowed_date
--     This table, is a junction table for a Many to Many relationship with the Book and Student tables : A student can borrow many books, and a book can be borrowed by many children
--     book_fk_id is a Foreign Key representing the column book_id from the Book table
--     student_fk_id is a Foreign Key representing the column student_id from the Student table
--     The pair of Foreign Keys is the Primary Key of the Junction Table


--  6. Add 4 records in the junction table, use subqueries.

--     the student named John, borrowed the book Alice In Wonderland on the 15/02/2022
--     the student named Bob, borrowed the book To kill a mockingbird on the 03/03/2021
--     the student named Lera, borrowed the book Alice In Wonderland on the 23/05/2021
--     the student named Bob, borrowed the book Harry Potter the on 12/08/2021

--  7. Display the data

--     Select all the columns from the junction table
--     Select the name of the student and the title of the borrowed books
--     Select the average age of the children, that borrowed the book Alice in Wonderland
--     Delete a student from the Student table, what happened in the junction table ?





--ANSWERS:
--Part 1

--1
CREATE TABLE customer (
id serial primary key,
first_name varChar,
last_name varChar not null);

--2
CREATE TABLE customer_profile (
id serial primary key,
isLoggedIn bool DEFAULT false,
customer_id int REFERENCES Customer(id));

--3
INSERT INTO Customer(first_name, last_name)
VALUES('John','Doe'),('Jerome', 'Lalu'), ('Lea', 'Rive');
INSERT INTO Customer_profile(isLoggedIn, customer_id)
VALUES(true, (SELECT id FROM customer WHERE first_name = 'John')),(false ,(SELECT id FROM customer WHERE first_name = 'Jerome'));

--4
SELECT first_name , isLoggedIn from customer LEFT JOIN customer_profile ON customer.id = customer_profile.customer_id; 
SELECT COUNT(*) from customer_profile WHERE isLoggedIn = false 








--Part 2


--1
CREATE TABLE book(book_id serial primary key , title varChar NOT NULL , author varChar NOT NULL);

--2
INSERT INTO book(title , author) VALUES ('Alice In Wonderland','Lewis Carroll'),('Harry Potter','J.K Rowling'),('To Kill a mockingbird','Harper Lee');

--3
CREATE TABLE students(student_id SERIAL PRIMARY KEY, name varChar NOT NULL UNIQUE , age int check(age <= 15));

--4
INSERT INTO students(name,age) VALUES ('John',12),('Lera',11),('Patrick',10),('Bob',14);

--5
CREATE TABLE library(book_fk_id int REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE ,
					 student_id int REFERENCES students(student_id) ON DELETE CASCADE ON UPDATE CASCADE ,
					 borrowed_date date);

--6
INSERT INTO library (book_fk_id , student_id , borrowed_date) VALUES

((SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),(SELECT student_id FROM students WHERE name = 'John'),('2022-02-15')),
((SELECT book_id FROM book WHERE title = 'To Kill a mockingbird'),(SELECT student_id FROM students WHERE name = 'Bob'),('2021-03-03')),
((SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),(SELECT student_id FROM students WHERE name = 'Lera'),('2021-05-23')),
((SELECT book_id FROM book WHERE title = 'Harry Potter'),(SELECT student_id FROM students WHERE name = 'Bob'),('2021-08-12'));

--7
SELECT * FROM library;
SELECT name , title FROM library JOIN students ON library.student_id = students.student_id JOIN book ON library.book_fk_id = book.book_id;
SELECT AVG(age) AS aiw_readers_average_age FROM library JOIN students ON library.student_id = students.student_id JOIN book ON library.book_fk_id = book.book_id WHERE title = 'Alice In Wonderland';
DELETE FROM students WHERE name = 'Bob'; -- The recods of bob in the library table were delted as well.
