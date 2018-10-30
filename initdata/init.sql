CREATE DATABASE kurd_word;
-- CREATE USER docker WITH PASSWORD 'docker';
GRANT ALL PRIVILEGES ON DATABASE "kurd_word" to docker;
\i create_tables.sql