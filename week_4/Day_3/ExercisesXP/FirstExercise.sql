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

CREATE TABLE customer_review(review_id serial primary key,
							film_id int,
							language_id references language(language_id),
							title varChar,
							score )


-- SELECT name FROM film JOIN language ON film.language_id = language.language_id GROUP BY name;
-- SELECT title , description , name AS language FROM film JOIN language ON film.language_id = language.language_id;
-- SELECT title , description , name AS language FROM film LEFT JOIN language ON film.language_id = language.language_id;
-- SELECT title , description , name AS language FROM film RIGHT JOIN language ON film.language_id = language.language_id;

-- CREATE TABLE new_film(id serial primary key , name varChar);
-- INSERT INTO new_film (name) VALUES ('Alice In Wonderland') , ('Jalied In the Minds') , ('VarChar on it')

