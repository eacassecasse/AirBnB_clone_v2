-- This script prepares a MYSQL Development Server for the project
-- This preparation is done creating a new user `hbnb_test`
-- with all privileges on the new database `hbnb_test_db` (to be created)
-- and SELECT privilege on `performance_schema` without failing if both
-- database and user exists
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`; -- Creates the database

-- Creates the user `hbnb_test`
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grants privileges on the `performance_schema` and `hbnb_test_db` to `hbnb_test`
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';

-- Persist the privileges
FLUSH PRIVILEGES;