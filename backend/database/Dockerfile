# Используем официальный образ PostgreSQL
FROM postgres:17

# Копируем SQL скрипт для инициализации
COPY init.sql /docker-entrypoint-initdb.d/
