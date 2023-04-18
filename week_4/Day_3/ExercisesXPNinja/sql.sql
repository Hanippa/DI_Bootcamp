-- Exercise 1 : DVD Rentals
-- Instructions

-- We want to encourage families and kids to enjoy our movies.

--     Retrieve all films with a rating of G or PG, which are are not currently rented (they have been returned/have never been borrowed).

--     Create a new table which will represent a waiting list for children’s movies. This will allow a child to add their name to the list until the DVD is available (has been returned). Once the child takes the DVD, their name should be removed from the waiting list (ideally using triggers, but we have not learned about them yet. Let’s assume that our Python program will manage this). Which table references should be included?

--     Retrieve the number of people waiting for each children’s DVD. Test this by adding rows to the table that you created in question 2 above.


SELECT * FROM film 
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
WHERE (rating = 'G' OR rating = 'PG') AND (return_date IS NOT NULL OR (return_date IS NULL AND rental_date IS NULL))

CREATE TABLE waiting_list(
first_name varChar(45) ,
last_name varChar(45),
movie_id int references film(film_id)
);

INSERT INTO waiting_list (first_name,last_name,movie_id) VALUES ('Dekel' , 'Matslich' , 19) , ('Patricia' , 'Jhonson' , 19)
SELECT count(*) FROM waiting_list GROUP BY movie_id;