-- We will use the newly installed dvdrental database.

--     In the dvdrental database write a query to select all the columns from the “customer” table.

--     Write a query to display the names (first_name, last_name) using an alias named “full_name”.

--     Lets get all the dates that accounts were created. Write a query to select all the create_date from the “customer” table (there should be no duplicates).

--     Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.

--     Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.

--     Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.

--     Write a query to retrieve all movie details where the movie id is either 15 or 150.

--     Write a query which should check if your favorite movie exists in the database. Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.

--     No luck finding your movie? Maybe you made a mistake spelling the name. Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.

--     Write a query which will find the 10 cheapest movies.

--     Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
--     Bonus: Try to not use LIMIT.

--     Write a query which will join the data in the customer table and the payment table. You want to get the first name and last name from the curstomer table, as well as the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).

--     You need to check your inventory. Write a query to get all the movies which are not in inventory.

--     Write a query to find which city is in which country.

--     Bonus You want to be able to see how your sellers have been doing? Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff member who sold them the dvd.




SELECT * FROM customer;
SELECT CONCAT(first_name,' ', last_name) as full_name from customer;
SELECT create_date FROM customer GROUP BY create_date;
SELECT * FROM customer ORDER BY first_name DESC;
SELECT film_id, title, description, release_year, rental_rate from film ORDER BY rental_rate ASC;
SELECT first_name ,phone FROM customer JOIN address ON customer.address_id = address.city_id WHERE district = 'Texas';
SELECT * FROM film WHERE film_id = 15 or film_id = 150;
SELECT film_id , title, description, length, rental_rate from film WHERE title = 'Naurasika of the vally of the wind';
SELECT film_id , title, description, length, rental_rate from film WHERE title LIKE 'Wi%';
SELECT * from film ORDER BY rental_rate LIMIT 10;
SELECT * from film ORDER BY rental_rate LIMIT 10 OFFSET 10;


SELECT first_name , last_name , amount , payment_date FROM customer JOIN payment ON customer.customer_id = payment.customer_id ORDER BY payment.payment_id;
SELECT * FROM film JOIN inventory ON film.film_id = inventory.film_id WHERE inventory.film_id IS NULL;
SELECT country, city FROM country JOIN city ON country.country_id = city.country_id;
SELECT staff_id , amount , payment_date ,first_name , last_name , customer.customer_id FROM customer JOIN payment ON customer.customer_id = payment.customer_id



