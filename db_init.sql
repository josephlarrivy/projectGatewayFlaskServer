-- psql -U postgres -d gatewayprojectflaskdatabase -f db_init.sql

DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS sports CASCADE;

CREATE TABLE users (
    user_id VARCHAR(255) PRIMARY KEY
);

CREATE TABLE sports (
    sport_id SERIAL PRIMARY KEY,
    sport_name VARCHAR(100) UNIQUE NOT NULL
);