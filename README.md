# Well

## Зависимости

* [Docker](https://www.docker.com/).
* [Docker Compose](https://docs.docker.com/compose/install/).
* [Poetry](https://python-poetry.org/) for Python package and environment management.

## Разработка

* Добавьте .env файл со следующими переменными окружения:
```console
# Строки подключения к БД
POSTGRES_URL
TEST_POSTGRES_URL

# Строка подключения для postgres имеет следующий вид:
# postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}
```



* Запустите сервис со всеми зависимостями:

```console
$ docker-compose up --build
```

* Добавить [pre-commit](https://github.com/pre-commit/pre-commit) хук
```console
$ pre-commit install
```

## Тесты

Тестирование проводится с помощью pytest, тесты размещаются в директории tests

Для тестирования необходимо предварительно зайти внутрь контейнера и запустить команду `pytest .`

```console
$ docker exec <FastAPI container ID> bash
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

* Postgres
```
$ alembic -n postgres revision --autogenerate -m "text"
$ alembic -n postgres upgrade head
$ alembic -n postgres downgrade -1
```
