-- 🌟 Exercise 1: DVD Rental
-- Instructions

--     Get a list of all film languages.

--     Get a list of all films joined with their languages – select the following details : film title, description, and language name. Try your query with different joins:
--         Get all films, even if they don’t have languages.
--         Get all languages, even if there are no films in those languages.

-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.


-- Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
-- It should have the following columns:

--     review_id – a primary key, non null, auto-increment.
--     film_id – references the new_film table. The film that is being reviewed.
--     language_id – references the language table. What language the review is in.
--     title – the title of the review.
--     score – the rating of the review (1-10).
--     review_text – the text of the review. No limit on the length.
--     last_update – when the review was last updated.


-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.

-- Delete a film that has a review from the new_film table, what happens to the customer_review table?
	



SELECT name FROM film JOIN language ON film.language_id = language.language_id GROUP BY name;
SELECT title , description , name AS language FROM film JOIN language ON film.language_id = language.language_id;
SELECT title , description , name AS language FROM film LEFT JOIN language ON film.language_id = language.language_id;
SELECT title , description , name AS language FROM film RIGHT JOIN language ON film.language_id = language.language_id;

CREATE TABLE new_film(id serial primary key , name varChar);
INSERT INTO new_film (name) VALUES ('Alice In Wonderland') , ('Jalied In the Minds') , ('VarChar on it')

CREATE TABLE customer_review(review_id serial primary key,
							film_id int references film(film_id) ON DELETE CASCADE,
							language_id int references language(language_id),
							title varChar,
							score int,
							review_text text,
							last_update date);
INSERT INTO customer_review(
							film_id,
							language_id,
							title,
							score,
							review_text,
							last_update) 
							VALUES
							(30,2,'Shit movie',0,'Piece of garbage do not watch this and waste your time',NOW()),
							(101,3,'MID',0,'Go watch this movie if you want to have nightmares',NOW());
							

-- 🌟 Exercise 2 : DVD Rental
-- Instructions

--     Use UPDATE to change the language of some films. Make sure that you use valid languages.

--     Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
-- 	   We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
-- 		Find out how many rentals are still outstanding (ie. have not been returned to the store yet).

-- 		Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)

-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?

--     The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.

--     The 2nd film : A short documentary (less than 1 hour long), rated “R”.

--     The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.

--     The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.









--1
UPDATE film SET language_id = (SELECT language_id FROM language WHERE name = 'Mandarin') WHERE film_id = 10 or film_id = 13;

--2
---- The addresss forign key, It changees that way you insert date into the table by changing the way you type an address, you first need to add your address to the address table and only the add the id of the added address to the customer table.

--3
DROP TABLE customer_review; -- It worked, becuase the customer review is connecter to another table and not vice versa.

--4
SELECT COUNT(*) from rental WHERE return_date is null;


--5
SELECT * from rental JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN film ON inventory.film_id = film.film_id
WHERE return_date is null ORDER BY rental_rate DESC LIMIT 30;



--6 - 1
SELECT * FROM film JOIN film_actor ON film.film_id = film_actor.film_id JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.first_name = 'Penelope' and actor.last_name = 'Monroe' and film.description LIKE '%Sumo%Wrestler%';


--6 - 2
SELECT * FROM film JOIN film_category ON film.film_id = film_category.film_id JOIN category ON film_category.category_id = category.category_id
WHERE film.rating = 'R' AND category.name='Documentary' AND film.length < 60;


--6 - 3
SELECT * FROM customer JOIN rental ON customer.customer_id = rental.customer_id 
JOIN inventory ON rental.inventory_id = inventory.inventory_id 
JOIN film  ON inventory.film_id = film.film_id
WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan'
AND film.rental_rate > 4
AND (rental.return_date > '2005-07-28' AND rental.return_date < '2005-08-01');


--6 - 4
SELECT * FROM customer JOIN rental ON customer.customer_id = rental.customer_id 
JOIN inventory ON rental.inventory_id = inventory.inventory_id 
JOIN film  ON inventory.film_id = film.film_id
WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan'
AND (film.description like '%Boat%' or film.title like '%Boat%')
ORDER BY film.replacement_cost DESC LIMIT 1;



