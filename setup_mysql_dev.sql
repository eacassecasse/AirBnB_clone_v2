-- This script prepares a MYSQL Development Server for the project
-- This preparation is done creating a new user `hbnb_dev`
-- with all privileges on the new database `hbnb_dev_db` (to be created)
-- and SELECT privilege on `performance_schema` without failing if both
-- database and user exists
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`; -- Creates the database

-- Creates the user `hbnb_dev`
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grants privileges on the `performance_schema` and `hbnb_dev_db` to `hbnb_dev`
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';

-- Persist the privileges
FLUSH PRIVILEGES;