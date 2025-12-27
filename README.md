# Automation-JSONPlaceholder

📋 Описание

Автоматизированное тестирование тестового [проекта](https://jsonplaceholder.typicode.com/) для практики с использованием Pytest, Requests, Pydantic, Allure.


🛠️ Технологический стек

```
Python 3.11+ - язык программирования
Pytest - фреймворк для тестирования
Requests - API тестирование
Pydantic - валидация данных
Allure - отчёты
```

📦 Установка

Требования
```
Python 3.11+
pip
```

Шаги установки
```
1) Клонировать репозиторий:

git clone https://github.com/MVGIC/Automation-JSONPlaceholder.git
cd Automation-JSONPlaceholder

2) Создать виртуальное окружение:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows

3) Установить зависимости:

pip install -r requirements.txt
```


🚀 Запуск тестов
```
Все тесты
pytest

Тесты с маркерами
pytest -m smoke           # Smoke-тесты
pytest -m regression      # Регрессионные тесты
pytest -m "not slow"      # Исключить медленные тесты

Параллельный запуск
pytest -n 4               # 4 процесса параллельно

С отчётом Allure
pytest --alluredir==test_results
allure serve test_results
```

📊 Отчёты

```
Генерация отчёта
pytest --alluredir=test_results

Просмотр отчёта
allure serve test_results
```


**CI Status:**

[![Python application](https://github.com/MVGIC/Automation-JSONPlaceholder/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/MVGIC/Automation-JSONPlaceholder/actions/workflows/python-app.yml)
