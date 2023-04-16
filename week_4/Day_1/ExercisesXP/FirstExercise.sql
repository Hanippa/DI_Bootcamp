CREATE TABLE items(id serial primary key,item_name varChar,price money);
CREATE TABLE customers(id serial primary key,first_name varChar,surname varChar);
INSERT INTO items(item_name,price)
VALUES ('Small Desk' , 100),('Large Desk' , 300),('Fan' , 80);
INSERT INTO customers(first_name,surname)
VALUES ('Greg' , 'Jones'),('Sandra' , 'Jones'),('Scott' , 'Scott'),('Trevor' , 'Green'),('Melanie' , 'Johnson');

SELECT * FROM items;
SELECT * FROM items WHERE price > money(80);
SELECT * FROM items WHERE price < money(300);
SELECT * FROM customers WHERE surname = 'Smith';
SELECT * FROM customers WHERE surname = 'Jones';
SELECT * FROM customers WHERE first_name != 'Scott'

--         All the items.
--         All the items with a price above 80 (80 not included).
--         All the items with a price below 300. (300 included)
--         All customers whose last name is ‘Smith’ (What will be your outcome?).
--         All customers whose last name is ‘Jones’.
--         All customers whose firstname is not ‘Scott’.


