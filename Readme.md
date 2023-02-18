# software engineering of control systems
## stack
* Fast api
* Docker
* REST API
* Uvicorn
* Postgres
## Start program
* создание виртуального кружения 
python -m venv .venv
* активация окружения
.venv/Scripts/activate
* установка зависимостей
pip install -r requirments.txt
* запустить сервер 
uvicorn main:app --reload
## Start tests
* запуск тестов для lab1
pytest .\test\test_lab1.py 
