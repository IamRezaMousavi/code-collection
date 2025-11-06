CREATE DATABASE IF NOT EXISTS test_database;

-- For Admin user:
-- GRANT ALL ON *.* TO '[username]'@'localhost' IDENTIFIED BY '[password]' WITH GRANT OPTION;
-- FLUSH PRIVILEGES;

-- For Normal user:
SELECT user, host FROM mysql.user WHERE user = 'test_user';
CREATE USER IF NOT EXISTS 'test_user'@'localhost' IDENTIFIED BY '****'; -- use 'test_user'@'%' to connect from anywhere
GRANT SELECT, INSERT, UPDATE, DELETE, EXECUTE ON test_database.* TO 'test_user'@'localhost';
FLUSH PRIVILEGES;

SELECT user, host FROM mysql.user WHERE user = 'test_user';
SHOW GRANTS FOR 'test_user'@'localhost';

-- Delete user:
REVOKE ALL PRIVILEGES ON test_database.* FROM 'test_user'@'localhost';
DROP USER IF EXISTS 'test_user'@'localhost';
SELECT user, host FROM mysql.user WHERE user = 'test_user';

DROP DATABASE IF EXISTS test_database;
