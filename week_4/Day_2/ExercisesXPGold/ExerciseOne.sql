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