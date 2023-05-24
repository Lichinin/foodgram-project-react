# Foodgram

![example workflow](https://github.com/lichinin/foodgram-project-react/actions/workflows/foodgram.yml/badge.svg)

Адрес проекта: [http://84.201.159.2/](http://84.201.159.2/)

Документация по API: [http://84.201.159.2/api/docs/](http://84.201.159.2/api/docs/)

_______
Foodgram Project React - это веб-приложение для публикации, поиска и сохранения рецептов. Пользователи могут создавать свои аккаунты, добавлять рецепты, отмечать их как избранные и подписываться на других пользователей.

## Описание проекта
Foodgram предоставляет следующие функциональности:

- Регистрация и аутентификация пользователей
- Создание, редактирование и удаление рецептов
- Поиск рецептов по различным критериям (название, ингредиенты и т. д.)
- Добавление рецептов в список избранных
- Подписка на других пользователей и просмотр их рецептов
- Генерация списка покупок на основе выбранных рецептов

## Развернуть проект на удаленном сервере

- Клонируйте репозиторий:
```
https://github.com/Lichinin/foodgram-project-react.git
```

- Установите на сервере Docker:

```
sudo apt install curl
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
sudo apt remove docker docker-engine docker.io containerd runc
sudo apt update
```

 - Установите необходимые пакеты для загрузки через https:
 ```
sudo apt install \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg-agent \
  software-properties-common -y 
```

- Добавьте ключ GPG для подтверждения подлинности в процессе установки:
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

- Добавьте репозиторий Docker в пакеты apt и обновите индекс пакетов:
```
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
```

- Установите Docker и Docker Compose:
```
sudo apt install docker-ce docker-compose -y
```

- Из папки infra скопируйте на сервер файлы docker-compose.yml, nginx.conf:

```
scp docker-compose.yml nginx.conf username@SERVER_IP:/home/username/
```

- Из корневой директории проекта скопируйте на сервер папку docs:

```
scp -r docs username@SERVER_IP:/home/username/
```

- В GitHub Actions создайте переменные окружения:
```
SECRET_KEY              # секретный ключ Django проекта
DOCKER_PASSWORD         # пароль от Docker Hub
DOCKER_USERNAME         # логин Docker Hub
HOST                    # публичный IP-адрес сервера
USER                    # имя пользователя на сервере
PASSPHRASE              # *если ssh-ключ защищен паролем
SSH_KEY                 # приватный ssh-ключ
TELEGRAM_TO             # ID телеграм-аккаунта для посылки сообщения
TELEGRAM_TOKEN          # токен бота, посылающего сообщение

DB_ENGINE               # django.db.backends.postgresql
POSTGRES_DB             # foodgram
POSTGRES_USER           # foodgram_user
POSTGRES_PASSWORD       # foodgram
DB_HOST                 # db
DB_PORT                 # 5432 (порт по умолчанию)
```

- Запуск Docker Compose на сервере
```
sudo docker compose up -d
```

- Выполните миграции:
```
sudo docker compose exec backend python manage.py migrate
```

- Создайте суперпользователя:
```
sudo docker compose exec backend python manage.py createsuperuser
```

- Соберите статику:
```
sudo docker compose exec backend python manage.py collectstatic --noinput
```

- Наполнить базу данных содержимым из файла ingredients.json:
```
sudo docker-compose exec backend python manage.py import_ingredients_csv
```

### Автор (backend):

Личинин Виталий
 