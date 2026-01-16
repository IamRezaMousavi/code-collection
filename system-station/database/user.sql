CREATE DATABASE IF NOT EXISTS test_database;

-- List users
SELECT user, host FROM mysql.user;

-- Create Admin user
-- GRANT ALL ON *.* TO '[username]'@'localhost' IDENTIFIED BY '[password]' WITH GRANT OPTION;
-- FLUSH PRIVILEGES;

-- Create Normal user
-- Host usaully localhost or % (to allow access from any host)
CREATE USER IF NOT EXISTS 'test_user'@'localhost' IDENTIFIED BY '****';

-- Change user password
-- ALTER USER 'test_user'@'localhost' IDENTIFIED BY 'newpassword';

-- Grant privileges to a user
-- Privileges such as ALL PRIVILEGES, SELECT, INSERT, UPDATE, DELETE, EXECUTE
GRANT SELECT, INSERT, UPDATE, DELETE, EXECUTE ON test_database.* TO 'test_user'@'localhost';
FLUSH PRIVILEGES; -- apply changes to privileges

-- Show privileges to a user
SHOW GRANTS FOR 'test_user'@'localhost';

-- Revoke privileges from a user
REVOKE SELECT, INSERT, UPDATE, DELETE, EXECUTE ON test_database.* FROM 'test_user'@'localhost';

-- Lock user
-- ALTER USER 'test_user'@'localhost' ACCOUNT LOCK;

-- Unock user
-- ALTER USER 'test_user'@'localhost' ACCOUNT UNLOCK;

-- Rename user
RENAME USER 'test_user'@'localhost' TO 'newtest_user'@'localhost';

-- Delete user
DROP USER IF EXISTS 'newtest_user'@'localhost';

DROP DATABASE IF EXISTS test_database;
