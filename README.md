# Тестирование moodle команда B.

![pytest](https://github.com/eximius8/team_b_testing_assignment/actions/workflows/python-app.yml/badge.svg)

Данный репозиторий содержит набор автотестов для тестирования системы [moodle](https://moodle.org/). В частности тестируется сайт: [qacoursemoodle.innopolis.university](https://qacoursemoodle.innopolis.university/), используемый [Университетом Иннополис](https://innopolis.university/).

##  Настройка

### Подготовка виртуального окружения

Для Ubuntu установить python3-venv:

```
sudo apt-get install python3-venv
```

Создать виртуальное окружение в папке проекта, обновить pip, установить зависимости:

```
python3 -m venv env
pip install -U pip
pip install -r requirements.txt
```

### Настройка pre-commit
pre-commit установит хуки для проверки кода. Каждый раз, когда разработчик будет делать очередной commit будет проходить проверка созданного кода автоматическими линтерами.
```
pre-commit install
```

### Запуск тестов

```
pytest --headless=false --base-url=https://qacoursemoodle.innopolis.university
```
Параметры `--headless` - (по умолчанию true) запуск тестов в режиме без демонстрации браузера `--base-url` - адрес сайта для тестирования (по умолчанию https://qacoursemoodle.innopolis.university), `--username`, `--password` - имя пользователя и пароль для входа в личный кабинет.
