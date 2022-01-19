-- Database: flask

-- DROP DATABASE IF EXISTS flask;

CREATE DATABASE flask
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

GRANT ALL ON DATABASE flask TO postgres;

GRANT TEMPORARY, CONNECT ON DATABASE flask TO PUBLIC;

CREATE USER yekog with encrypted password 'yekog';

GRANT ALL ON DATABASE flask TO yekog;