-- Exercise 1 : Bonus Public Database (Continuation of XP)

--     Fetch the last 2 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
--     Use SQL to delete all purchases made by Scott.
--     Does Scott still exist in the customers table, even though he has been deleted? Try and find him.
--     Use SQL to find all purchases. Join purchases with the customers table, so that Scott’s order will appear, although instead of the customer’s first and last name, you should only see empty/blank. (Which kind of join should you use?).
--     Use SQL to find all purchases. Join purchases with the customers table, so that Scott’s order will NOT appear. (Which kind of join should you use?)

SELECT first_name , surname FROM customers ORDER BY first_name DESC FETCH FIRST 2 ROWS ONLY;
DELETE FROM purchases WHERE customer_id = (SELECT id from customers WHERE first_name = 'Scott') returning *;
SELECT * FROM customers WHERE customers.first_name = 'Scott';
SELECT * FROM customers LEFT JOIN purchases  ON purchases.customer_id = customers.id WHERE customers.first_name = 'Scott'; --LEFT Join
SELECT * FROM customers RIGHT JOIN purchases  ON purchases.customer_id = customers.id WHERE customers.first_name = 'Scott'; -- RIGHT Join