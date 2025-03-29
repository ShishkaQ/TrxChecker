-- Создание базы данных
CREATE DATABASE trondb WITH ENCODING 'UTF8';

-- Подключение к базе данных
\c trondb;

-- Таблица пользователей
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    address TEXT,
    bandwidth TEXT,
    energy TEXT,
    balance FLOAT
);

