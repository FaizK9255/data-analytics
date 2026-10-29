/* 
1. The name of the table that holds items northwind  sells is products, with the UnitsOnOrder column.
2. The name of the table that holds the types/categories of the items northwind  sells is orderdetails
*/

SELECT *
FROM employees;
-- Margaret Peacock

SELECT *
FROM products
LIMIT 10;
-- It returned 1000, but you can change the rows returned in the limit section at the top of the query pane

SELECT *
FROM categories;
-- The category ID for seafood is 8

SELECT OrderID,
OrderDate,
Shipname,
Shipcountry
FROM orders
LIMIT 50;
