# Backend
## Установка
1. Перейдите в директорию с бекендом:
```bash
cd backend
```
2. Создайте виртуальную среду:
```bash
python3 -m venv trx
```
3. Активируйте среду:
```bash
source trx/bin/activate
```
```bash
trx\Scripts\activate
```
4. Установите нужные библиотеки:
```bash
pip install -r requirements.txt
```
5. Перейдите в TrxChecker
```bash
cd ../
```
5. Запустите бекенд сервер:
```bash
uvicorn backend.app.main:app --reload
```

# Tests
## Запуск тестов
1. Перейдите в корневую папку:
```bash
cd TrxChecker
```
2. Запустить тесты
```bash
pytest backend/tests/test_api.py -v
```
