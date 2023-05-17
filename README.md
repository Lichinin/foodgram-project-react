# Foodgram

## Описание проекта
 «Продуктовый помощник»
 
Социальная сеть для публикации рецептов

## Установка

Перейти в каталог `backend`
Cоздать и активировать виртуальное окружение:
```
python -m venv env
source env/Scripts/activate
```
Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции:
```
python manage.py migrate
```
Запустить проект:
```
python manage.py runserver
```
Перейти в каталог infra-dev

Собрать и запустить контейнеры
```
docker-compose up
```
Перейтиде в папку `backend`. Запустите сервер:
```
python manage.py runserver
```
Документация по API будет доступна по адресу `localhost/api/redoc/` 