-- CREATE TABLE items(id serial primary key,item_name varChar,price money);
-- CREATE TABLE customers(id serial primary key,first_name varChar,surname varChar);
-- INSERT INTO items(item_name,price)
-- VALUES ('Small Desk' , 100),('Large Desk' , 300),('Fan' , 80);
-- INSERT INTO customers(first_name,surname)
-- VALUES ('Greg' , 'Jones'),('Sandra' , 'Jones'),('Scott' , 'Scott'),('Trevor' , 'Green'),('Melanie' , 'Johnson');

-- SELECT * FROM items;
-- SELECT * FROM items WHERE price > money(80);
-- SELECT * FROM items WHERE price < money(300);
-- SELECT * FROM customers WHERE surname = 'Smith';
-- SELECT * FROM customers WHERE surname = 'Jones';
-- SELECT * FROM customers WHERE first_name != 'Scott'

--         All the items.
--         All the items with a price above 80 (80 not included).
--         All the items with a price below 300. (300 included)
--         All customers whose last name is ‘Smith’ (What will be your outcome?).
--         All customers whose last name is ‘Jones’.
--         All customers whose firstname is not ‘Scott’.




-- 🌟 Exercise 1 : Items and customers
-- Instructions

-- We will work on the public database that we created yesterday.

--     Use SQL to get the following from the database:
--         All items, ordered by price (lowest to highest).
--         Items with a price above 80 (80 included), ordered by price (highest to lowest).
--         The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
--         All last names (no other columns!), in reverse alphabetical order (Z-A)

SELECT * FROM items ORDER BY price;
SELECT * FROM items WHERE price >= money(80) ORDER BY price DESC;
SELECT item_name, price FROM items ORDER BY item_name LIMIT 3;
SELECT surname from customers ORDER BY surname 
