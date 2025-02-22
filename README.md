![Static Badge](https://img.shields.io/badge/Python-3.11.4-orange) ![Static Badge](https://img.shields.io/badge/Aiogram-3.2.0-blue) ![Static Badge](https://img.shields.io/badge/Django-5.0-blue) ![Static Badge](https://img.shields.io/badge/Django_CKEditor-6.7.0-blue)  ![Static Badge](https://img.shields.io/badge/PostgreSQL-14.15-purple) ![Static Badge](https://img.shields.io/badge/Redis-6.0.16-purple)

[Василий Питонов](https://t.me/vaspytbot) – Telegram-бот для подготовки к ЕГЭ по информатике. Он позволяет решать задания из [Открытого банка тестовых заданий](https://ege.fipi.ru/bank) как с выбором ответа, так и с кратким ответом. 

## Основные возможности
:blue_book:  Выбор раздела заданий  
:infinity: Бесконечный режим из случайных заданий  
:bar_chart: Просмотр статистики по каждому из разделов  
:repeat: Сброс прогресса по решенным разделам  
:computer: Панель администратора в виде веб-приложения   
:pencil2: HTML-редактор текста задания с учётом тегов, поддерживаемых Telegram

## Запуск 
1. Клонируйте репозиторий:
```
git clone https://github.com/khaustova/ege-informatics-bot.git
```
2. Переименуйте файл `.env.example` в `.env` и добавьте свои данные.
3. Если бот ещё не создан, то создайте его:
   * Найдите @BotFather в Telegram.
   * Используйте команду `/newbot`, чтобы создать нового бота.
   * Вставьте полученный токен в переменную `BOT_TOKEN` в файле `.env`. 
4. Запустите проект в Docker:
```
docker-compose up --build
```
5. Панель администратора будет доступна по адресу http://127.0.0.1:8000. Сам бот будет работать в Telegram.

