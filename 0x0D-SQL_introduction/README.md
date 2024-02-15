What's a database?

A database is an organized collection of structured information or data, typically stored electronically in a computer system. It is designed to efficiently manage, store, and retrieve data.
What's a relational database?

A relational database is a type of database that stores and organizes data into tables consisting of rows and columns. It establishes relationships between tables using keys, enabling the storage and retrieval of related data.
What does SQL stand for?

SQL stands for Structured Query Language. It is a standard language used for managing relational databases. SQL allows users to perform various operations such as querying data, defining schema, modifying data, and controlling access to the database.
What's MySQL?

MySQL is an open-source relational database management system (RDBMS) that uses SQL. It is widely used for web-based applications and is known for its reliability, performance, and ease of use. MySQL is developed, distributed, and supported by Oracle Corporation.
How to create a database in MySQL?

You can create a database in MySQL using the CREATE DATABASE statement followed by the database name. For example:
sql
Copy code
CREATE DATABASE mydatabase;
What does DDL and DML stand for?

DDL stands for Data Definition Language. It includes SQL commands used to define, modify, and manage the structure of database objects such as tables, indexes, and views.
DML stands for Data Manipulation Language. It includes SQL commands used to manipulate data stored in the database, such as inserting, updating, deleting, and querying data.
How to CREATE or ALTER a table?

To create a table, you can use the CREATE TABLE statement followed by the table name and its columns. For example:
sql
Copy code
CREATE TABLE mytable (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);
To alter a table, you can use the ALTER TABLE statement followed by the table name and the alteration you want to make. For example:
sql
Copy code
ALTER TABLE mytable ADD COLUMN age INT;
How to SELECT data from a table?

To select data from a table, you can use the SELECT statement followed by the columns you want to retrieve and the table name. For example:
sql
Copy code
SELECT * FROM mytable;
How to INSERT, UPDATE or DELETE data?

To insert data into a table, you can use the INSERT INTO statement followed by the table name and the values to insert. For example:
sql
Copy code
INSERT INTO mytable (id, name) VALUES (1, 'John');
To update data in a table, you can use the UPDATE statement followed by the table name and the new values. For example:
sql
Copy code
UPDATE mytable SET name = 'Jane' WHERE id = 1;
To delete data from a table, you can use the DELETE FROM statement followed by the table name and a condition to specify which rows to delete. For example:
sql
Copy code
DELETE FROM mytable WHERE id = 1;
What are subqueries?

Subqueries, also known as nested queries or inner queries, are SQL queries nested within another query. They are used to retrieve data based on the results of another query. Subqueries can be used in SELECT, INSERT, UPDATE, or DELETE statements.
How to use MySQL functions?

MySQL provides a wide range of built-in functions for performing various operations on data. You can use functions such as mathematical functions, string functions, date and time functions, aggregate functions, etc., in your SQL queries. For example:
sql
Copy code
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM employees;
This query uses the CONCAT function to concatenate the first_name and last_name columns into a single column called full_name.





