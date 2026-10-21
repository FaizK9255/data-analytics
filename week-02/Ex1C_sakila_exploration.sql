/*
a) In the columns section of  actor, it includes the following: actor_id, first_name, last_name, and last_update. 
b) In the columns section of film, it includes the following: film_id, title, description, release_year, language_id, original_language_id, 
rental_duration, rental_rate, length, replacement_cost, rating, special_features, and last_update. 
c) The film_actor table also contains actor_id and film_id.
d) The rental table returned 1000 rows, and 7 columns labeled rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, and last_update
e) The inventory table also returned 1000 rows, with 4 columns labeled inventory_id, film_id, store_id, and last_update.
f) 	 To be able to understand the names of all films that were rented on a specific date, one would only need the film table and tthe rental table.
*/

SELECT * FROM film;
SELECT * FROM rental; 