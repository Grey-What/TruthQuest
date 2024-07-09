-- this script prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS TruthQuest_db;
-- creating new user named : TQ_Admin with all privileges on the db TruthQuest_db
-- with the password : TQ_Admin_pwd if it dosen't exist
CREATE USER IF NOT EXISTS 'TQ_Admin'@'localhost' IDENTIFIED BY 'TruthQuest24';
-- granting all privileges to the new user
GRANT ALL PRIVILEGES ON TruthQuest_db.* TO 'TQ_Admin'@'localhost';
FLUSH PRIVILEGES;
-- granting the SELECT privilege for the user TQ_Admin in the db performance_schema
GRANT SELECT ON performance_schema.* TO 'TQ_Admin'@'localhost';
FLUSH PRIVILEGES;
