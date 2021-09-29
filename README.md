# Тестирование moodle команда B.

![pytest](https://github.com/eximius8/team_b_testing_assignment/actions/workflows/python-app.yml/badge.svg)

Тестируемый сайт: [qacoursemoodle.innopolis.university](https://qacoursemoodle.innopolis.university/)

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

```
pre-commit install
```

### Запуск тестов

```
pytest --headless=false --base-url=https://qacoursemoodle.innopolis.university
```
Параметры `--headless` - (по умолчанию true) запуск тестов в режиме без демонстрации браузера `--base-url` - адрес сайта для тестирования (по умолчанию https://qacoursemoodle.innopolis.university)
