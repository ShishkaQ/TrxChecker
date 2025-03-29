# PostgreSQL
## Создание контейнера с использованием Docker Compose

1. Убедитесь, что у вас установлены Docker и Docker Compose.
   Проверьте установку:
   ```bash
   docker --version
   docker-compose --version
   ```

2. Перейдите в директорию проекта:
   ```bash
   cd backend/database
   ```

3. Запустите контейнеры:
   Выполните команду:
   ```bash
   sudo docker-compose up -d
   ```

4. Проверьте статус контейнеров:
   Убедитесь, что контейнеры запущены:
   ```bash
   sudo docker-compose ps
   ```

5. Остановка контейнера
    ```bash
    sudo docker-compose down
    ```