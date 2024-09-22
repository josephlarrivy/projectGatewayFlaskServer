-- TO CREATE THIS DATABASE RUN: psql -h localhost -U josephlarrivy -d postgres -f db_init.sql
-- TO CONNECT TO PSQL IN THE TERMINAL AND VIEW THIS DATABASE RUN: psql -h localhost -U josephlarrivy -d gatewayprojectflaskdatabase 

-- Connect to the default "postgres" database (or another database that is not the one you want to drop)
\c postgres

-- Drop the existing database
DROP DATABASE IF EXISTS gatewayprojectflaskdatabase;

-- Recreate the database
CREATE DATABASE gatewayprojectflaskdatabase;

\c gatewayprojectflaskdatabase;

DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS sports CASCADE;

CREATE TABLE users (
    user_id VARCHAR(255) PRIMARY KEY
);

CREATE TABLE sports (
    sport_id SERIAL PRIMARY KEY,
    sport_name VARCHAR(100) UNIQUE NOT NULL
);

-- Insert some initial data into the Users table
INSERT INTO sports (sport_name) VALUES ('hockey');