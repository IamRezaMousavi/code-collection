CREATE DATABASE IF NOT EXISTS testdb;

-- Create table
CREATE TABLE IF NOT EXISTS testdb.users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20),
    birthday DATE,
    salary DOUBLE
);

-- Create row
INSERT INTO testdb.users
    (name, salary)
VALUES
    ("Reza", "15.2");

-- Read rows
SELECT * FROM testdb.users;

-- Update rows
UPDATE testdb.users
SET salary = salary+1
WHERE name = "Reza";

-- Delete Rows
DELETE FROM testdb.users
WHERE name = "Reza";

-- Delete table
DROP TABLE IF EXISTS testdb.users;

DROP DATABASE IF EXISTS testdb;
