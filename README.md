# Тестирование moodle команда B.

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
