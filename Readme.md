# Домашнее задание к лекции «Введение в БД. Типы БД»

1. [Введение в БД. Типы БД](./01-introduction)
1. [Работа с SQL. Создание БД](./02-creation)
1. [Select-запросы, выборки из одной таблицы](dml)
1. [Группировки, выборки из нескольких таблиц](dml-advanced)
1. [Select-запросы, выборки из одной таблицы](./03-dml)
1. [Продвинутая выборка данных](./04-dml-advanced)
1. [Работа с PostgreSQL из Python](./05-psycopg)
1. [Python и БД. ORM](./06-orm)

Необходимо установить PostgreSQL на свой ПК.

### Windows

[Видео-инструкция](https://embed.new.video/uyjUq9B3qYo6BbbkzG71Ny)

[Ссылка на PostgreSQL для Windows](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)

### Linux (на примере Ubuntu 20.04)

[Видео-инструкция](https://embed.new.video/cRQW4Z2YnxZUxzKRLWwnPF)

Команды для установки:

```bash
# PostgreSQL
sudo apt update && sudo apt install postgresql-12
# pgAdmin4
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" |sudo tee  /etc/apt/sources.list.d/pgdg.list
sudo apt update && sudo apt install pgadmin4
```

### Mac OS X

[Видео-инструкция](https://videos-bb5ddb7a.cdn.integros.com/videos/5x1n2qgzvEhGTeG71vhmBE/mp4/1080.mp4)

Команды для установки:

```bash
brew install postgres
postgres -V
pg_ctl -D /usr/local/var/postgres start
createuser -P -s postgres
```

## Установка DBeaver Community 

Установка DBeaver Community для работы с СУБД. Это бесплатная программа, вы можете заранее скачать ее [по ссылке](https://dbeaver.io/download/) и установить на свой компьютер.