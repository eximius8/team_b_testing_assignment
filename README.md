# Тестирование moodle команда B.

![pytest](https://github.com/eximius8/team_b_testing_assignment/actions/workflows/python-app.yml/badge.svg)

Данный репозиторий содержит набор автотестов для тестирования системы [moodle](https://moodle.org/). В частности тестируется сайт: [qacoursemoodle.innopolis.university](https://qacoursemoodle.innopolis.university/), используемый [Университетом Иннополис](https://innopolis.university/).

## Схема абстракций в проекте

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBNW3Rlc3RfYXV0aF9pbnZhbGlkXSAtLS0gQVxuICAgIE5bdGVzdF9hdXRoX3ZhbGlkXSAtLS0gQSAgIFxuICAgIEJbVGVzdEFkZFBlcnNvbmFsRGF0YV0gLS0tIEUgXG4gICAgT1tUZXN0QWRkTmV3Q291cnNlXSAtLS0gRSBcbiAgICAgQVtUZXN0QXV0aF0gLS0tIEUgXG4gICAgUVsuLi5dIC0tLSBPXG4gICAgTFsuLi5dIC0tLSBCXG4gICAgQ3vQpNC40LrRgdGC0YPRgNGLfSAtLT4gRVvQotC10YHRgtGLXSBcbiAgICBGW9Cf0YDQuNC70L7QttC10L3QuNC1IC0gQXBwbGljYXRpb25dIC0tPiBDIFxuICAgIEYgLS0-IERbQ3JlYXRlQ291cnNlUGFnZV1cbiAgICBGIC0tPiBHW0xvZ2luUGFnZV1cbiAgICBGIC0tPiBIW1VzZXJQYWdlXVxuICAgIEggLS0-IFhbLi4uXVxuICAgIEQgLS0-IEpb0JvQvtC60LDRgtC-0YDRi11cbiAgICBHIC0tPiBLW9Cb0L7QutCw0YLQvtGA0YtdXG4iLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlLCJhdXRvU3luYyI6dHJ1ZSwidXBkYXRlRGlhZ3JhbSI6ZmFsc2V9)](https://mermaid.live/edit/#eyJjb2RlIjoiZ3JhcGggVERcbiAgICBNW3Rlc3RfYXV0aF9pbnZhbGlkXSAtLS0gQVxuICAgIE5bdGVzdF9hdXRoX3ZhbGlkXSAtLS0gQSAgIFxuICAgIEJbVGVzdEFkZFBlcnNvbmFsRGF0YV0gLS0tIEUgXG4gICAgT1tUZXN0QWRkTmV3Q291cnNlXSAtLS0gRSBcbiAgICAgQVtUZXN0QXV0aF0gLS0tIEUgXG4gICAgUVsuLi5dIC0tLSBPXG4gICAgTFsuLi5dIC0tLSBCXG4gICAgQ3vQpNC40LrRgdGC0YPRgNGLfSAtLT4gRVvQotC10YHRgtGLXSBcbiAgICBGW9Cf0YDQuNC70L7QttC10L3QuNC1IC0gQXBwbGljYXRpb25dIC0tPiBDIFxuICAgIEYgLS0-IERbQ3JlYXRlQ291cnNlUGFnZV1cbiAgICBGIC0tPiBHW0xvZ2luUGFnZV1cbiAgICBGIC0tPiBIW1VzZXJQYWdlXVxuICAgIEggLS0-IFhbLi4uXVxuICAgIEQgLS0-IEpb0JvQvtC60LDRgtC-0YDRi11cbiAgICBHIC0tPiBLW9Cb0L7QutCw0YLQvtGA0YtdXG4iLCJtZXJtYWlkIjoie1xuICBcInRoZW1lXCI6IFwiZGVmYXVsdFwiXG59IiwidXBkYXRlRWRpdG9yIjpmYWxzZSwiYXV0b1N5bmMiOnRydWUsInVwZGF0ZURpYWdyYW0iOmZhbHNlfQ)

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
