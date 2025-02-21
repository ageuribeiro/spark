CREATE DATABASE IF NOT EXISTS clean_architecture;
USE clean_architecture;
CREATE TABLE IF NOT EXISTS users (
    id INT primary key identity,
    first_name VARCHAR(255) not null,
    last_name VARCHAR(255) not null,
    age INT not null,
    password VARCHAR(255) not null
);
