-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS TruthQuest_db;
CREATE USER IF NOT EXISTS 'TQ_Admin'@'localhost' IDENTIFIED BY 'TruthQuest24';
GRANT ALL PRIVILEGES ON `TruthQuest_db`.* TO 'TQ_Admin'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'TQ_Admin'@'localhost';
FLUSH PRIVILEGES;
