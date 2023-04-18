-- Exercise 1 : DVD Rentals
-- Instructions

--     Get a list of all rentals which are out (have not been returned). How do we identify these films in the database?

--     Get a list of all customers who have not returned their rentals. Make sure to group your results.

--     Get a list of all the Action films with Joe Swank.
--         Before you start, could there be a shortcut to getting this information? Maybe a view?

-- SELECT * FROM rental WHERE return_date IS NULL; -- We indetify them by an empty return date(null).

-- SELECT first_name , last_name FROM rental JOIN customer ON rental.customer_id = customer.customer_id WHERE return_date IS NULL GROUP BY first_name , last_name;

SELECT * FROM film JOIN film_category ON film_category.film_id = film.film_id JOIN category ON film_category.category_id = category.category_id
JOIN film_actor ON film_actor.film_id = film.film_id JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE category.name = 'Action' AND actor.first_name = 'Joe' AND actor.last_name = 'Swank';





-- Exercise 2 – Happy Halloween
-- Instructions

-- There is a zombie plague approaching! The DVD rental company is offering to lend all of its DVDs to the local shelters, so that the citizens can watch the movies together in the shelters until the zombies are destroyed by the armed forces. Prepare tables with the following data:

--     How many stores there are, and in which city and country they are located.

SELECT COUNT(*) FROM store;

SELECT country , city FROM store JOIN address ON store.address_id = address.address_id 
JOIN city ON address.city_id = city.city_id
JOIN country ON city.country_id = country.country_id; 

--     How many hours of viewing time there are in total in each store – in other words, the sum of the length of every inventory item in each store.

SELECT SUM(length) FROM inventory JOIN film ON inventory.film_id = film.film_id GROUP BY store_id;

--     Make sure to exclude any inventory items which are not yet returned. (Yes, even in the time of zombies there are people who do not return their DVDs)

SELECT SUM(length) FROM inventory JOIN film ON inventory.film_id = film.film_id JOIN rental ON inventory.inventory_id = rental.inventory_id  WHERE return_date IS NOT NULL GROUP BY store_id;

--     A list of all customers in the cities where the stores are located.

SELECT first_name , last_name FROM customer JOIN address ON customer.address_id = address.address_id JOIN city ON address.city_id = city.city_id
WHERE address.city_id IN (SELECT address.city_id from store JOIN address ON store.address_id = address.address_id JOIN city ON address.city_id = city.city_id);

--     A list of all customers in the countries where the stores are located.

SELECT first_name , last_name FROM customer JOIN address ON customer.address_id = address.address_id JOIN city ON address.city_id = city.city_id
WHERE country_id IN (SELECT country_id from store JOIN address ON store.address_id = address.address_id JOIN city ON address.city_id = city.city_id);

--     Some people will be frightened by watching scary movies while zombies walk the streets. Create a ‘safe list’ of all movies which do not include the ‘Horror’ category, or contain the words ‘beast’, ‘monster’, ‘ghost’, ‘dead’, ‘zombie’, or ‘undead’ in their titles or descriptions… Get the sum of their viewing time (length).
--     Hint : use the CHECK contraint

SELECT *  from film JOIN film_category ON film.film_id = film_category.film_id JOIN category ON film_category.category_id = category.category_id WHERE category.name != 'Horror' AND (description like '%Beast%' or description like '%Monster%' or description like '%Ghost%' or description like '%Dead%' or description like '%Zombie%' or description like '%Undead%');
SELECT SUM(length)  from film JOIN film_category ON film.film_id = film_category.film_id JOIN category ON film_category.category_id = category.category_id WHERE category.name != 'Horror' AND (description like '%Beast%' or description like '%Monster%' or description like '%Ghost%' or description like '%Dead%' or description like '%Zombie%' or description like '%Undead%');

--     For both the ‘general’ and the ‘safe’ lists above, also calculate the time in hours and days (not just minutes).
