# Well

## Зависимости

* [Docker](https://www.docker.com/).
* [Docker Compose](https://docs.docker.com/compose/install/).
* [Poetry](https://python-poetry.org/) for Python package and environment management.

## Разработка

* Запустите сервис со всеми зависимостями:

```console
$ docker-compose up
```

* Установите зависимости с poetry

```console
$ poetry install
```

* Добавить [pre-commit](https://github.com/pre-commit/pre-commit) хук
```console
$ pre-commit install
```

## Тесты

Тестирование проводится с помощью pytest, тесты размещаются в директории tests

Для тестирования необходимо предварительно зайти внутрь контейнера и запустить команду `pytest .`

```console
$ docker-compose exec internal_api sh
$ pytest .
```

## Структура проекта

```
-> *alembic* — папка с миграциями
-> *app*
   -> *api* — слой с логикой обработки запросов через api
   -> *core* — глобальные для проекта вещи, вроде настроек (`config.py`)
   -> *db* — инициализация базы и сессии (скорее всего в процессе работы над проектом изменяться не будет)
   -> *models* — модели в терминологии SQLAlchemy (не путать с *schemas* в pydantic и бизнес-моделями)
   -> *schemas* — схемы для валидации/сериализации объектов запроса/ответа (они же модели в терминологии pydantic)
   -> *services* — сервисный слой, здесь размещается вся бизнес-логика.
-> *tests* — корень для тестов
-> *.env.template* — файл для перечисления всех используемых внутри сервиса переменных среды
```

## Миграции

* После создания модели в `app/models` необходимо импортировать ее в `app/db/base.py` (для того, что сделать ее видимой для alembic) *todo: сделать автоимпорт для alembic, что убрать необходимость в импорте*

* Внутри контейнера запустить

```console
$ alembic -n postgres revision --autogenerate -m "Add column last_name to User model"
```

* Запустить миграцию

```console
$ alembic -n postgres upgrade head
```

## Makefile
* Сбилдить проект
```
$ make build
```
* Запустить проект
```
$ make run
```
* Создать миграции в одной из бд
```
$ make migrations postgres
```
* Выполнить миграции в одной из бд
```
$ make migrate postgres
```
* Откатить одну из бд на ревизию назад
```
$ make downgrade postgres
```
