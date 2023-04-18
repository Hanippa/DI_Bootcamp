-- Instructions

--     Create a table called product_orders and a table called items. You decide which fields should be in each table, although make sure the items table has a column called price.

--     There should be a one to many relationship between the product_orders table and the items table. An order can have many items, but an item can belong to only one order.

--     Create a function that returns the total price for a given order.

--     Bonus :
--         Create a table called users.
--         There should be a one to many relationship between the users table and the product_orders table.
--         Create a function that returns the total price for a given order of a given user.


CREATE TABLE product_orders(id serial primary key ,
							item_id int references items(id) ON DELETE NO ACTION,
							customer_id int references customers(id),
							"date" timestamp not null default CURRENT_TIMESTAMP);
INSERT INTO product_orders(item_id , customer_id) VALUES (1,(SELECT id from customers WHERE first_name = 'Melanie'))

create or replace function total_price(order_id int)
returns money as $$
	begin 
		return (SELECT price FROM product_orders JOIN items ON product_orders.item_id = items.id WHERE product_orders.id = order_id);
	end
$$ language plpgsql; 


SELECT total_price(1) from product_orders;